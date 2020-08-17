import tensorflow as tf

# setup the compuations graph
x = tf.Variable(3,name="x")
y = tf.Variable(4,name="y")

# define the function
f = x**2 + y - 3*x*y # 3^2 + 4 - 3*3*4 = -23

# init all variables
init = tf.global_variables_initializer()


# computation graph is finished, now obtain a session
with tf.Session() as sess:
    init.run() # init
    result = f.eval() # and obtain the result


print("************************")
print(result)
