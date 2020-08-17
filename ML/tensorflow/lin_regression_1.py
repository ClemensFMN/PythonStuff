import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# simple linear regression with tensorflow

# the true parameters
ktrue = 1.2
dtrue = 0.4

N = 10

# generate training data x & y
x_train = np.linspace(0,1,N)
y_train = ktrue * x_train + dtrue + np.random.normal(0, 0.1, N)



# now define the computaional graph
# in contrast to before, we model x & y as "generic"; i.e. not associated with data
x = tf.placeholder(tf.float32, shape=(None, ), name='x')
y = tf.placeholder(tf.float32, shape=(None, ), name='y')

k = tf.Variable(np.random.normal(), name='k')
d = tf.Variable(np.random.normal(), name='d')

# define a predictor & loss-function
y_pred = tf.add(tf.multiply(k, x), d)
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
    print(k.eval(), d.eval())
    # and setup a plot of training vs predicted data
    y_pred = session.run(y_pred, {x : x_train})
    plt.plot(x_train,y_train,'ro', x_train, y_pred,'-gx')
    plt.grid()
    plt.show()
    
