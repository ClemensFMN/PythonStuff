import tensorflow as tf

# we define a function y(x_1, x_2)
def fun_obj(x, c, A):
    with tf.GradientTape() as t:
        t1 = tf.linalg.matvec(A, (x-c))
        y = tf.tensordot(x-c, t1, axes=1) # y = 2(x_1 - 3)^2 + (x_2 - 1)^2 the gradient of this is [4x_1-12, 2x_2-2]

        y_grad = t.gradient(y, x)
        return (y, y_grad)


x = tf.constant([5.0, 2.0])
x = tf.Variable(x)

c = tf.constant([3.0, 1.0])
A = tf.constant([[2.0, 0.0], [0.0, 1.0]])


y, g = fun_obj(x, c, A)
#print(y) # calculate y @ x = [5,2] -> 2*2^2 + 1^2 = 9
#print(g) # calculate the gradient @ [5,2] -> [4*5-12, 2*2-2] = [8, 2]

# now we run a gradient descent algorithm

for k in range(100):
    print("k = ", k) # which iteration are we in
    y, g = fun_obj(x, c, A) # calc y & its gradient

    x.assign(x - 0.1*g) # this is REALLY important; x = x - 0.1*g does NOT work
    print("new x", x)
