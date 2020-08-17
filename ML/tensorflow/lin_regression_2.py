import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# now, let's make the linear dependency quadratic...

# the true parameters
k2true = 0.2
k1true = 1.2
dtrue = 0.4

N = 10

# generate training data x & y
x_train = np.linspace(0,1,N)
y_train = k2true * x_train**2 + k1true * x_train + dtrue + np.random.normal(0, 0.05, N)



# now define the computaional graph
# in contrast to before, we model x & y as "generic"; i.e. not associated with data
x = tf.placeholder(tf.float32, shape=(None, ), name='x')
y = tf.placeholder(tf.float32, shape=(None, ), name='y')

k1 = tf.Variable(np.random.normal(), name='k1')
k2 = tf.Variable(np.random.normal(), name='k2')
d = tf.Variable(np.random.normal(), name='d')

# define a predictor & loss-function
y_pred = tf.add(tf.add(tf.multiply(k1, x), tf.multiply(k2, tf.square(x))), d)
loss = tf.reduce_mean(tf.square(y_pred - y))

# and an optimizer and a training op which minimizes the loss
optimizer = tf.train.GradientDescentOptimizer(0.1)
train_op = optimizer.minimize(loss)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    # inside the session, we assign the training data the x & y placeholders
    feed_dict = {x: x_train, y: y_train}

    for i in range(1000):
        _ = session.run(train_op, feed_dict) # and run the training op
        if(i % 100 == 0):
            print(i, "loss:", loss.eval(feed_dict))

    # finally, we print the values k & d
    print(k2.eval(), k1.eval(), d.eval())
    # and setup a plot of training vs predicted data
    y_pred = session.run(y_pred, {x : x_train})
    plt.plot(x_train,y_train,'ro', x_train, y_pred,'-gx')
    plt.grid()
    plt.show()
    
