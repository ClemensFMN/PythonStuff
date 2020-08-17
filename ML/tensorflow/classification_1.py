import tensorflow as tf
from tensorflow.contrib.layers import fully_connected
import numpy as np
import matplotlib.pyplot as plt

# more complex classification example
# we have two classes of points separated by a plane ax + by = d

a = 1.0
b = 2.0
d = 1.0

# first we generate the training data
N = 100

p_train = np.random.uniform(low=-5.0, high=5.0, size=(N,2))
label_train = np.zeros(N)

for (ind, (x,y)) in enumerate(p_train):
    if(a*x + b*y < d):
        label_train[ind] = 0
    else:
        label_train[ind] = 1

#ind_zero = np.where(label_train == 0)
#p_zero = p_train[ind_zero]
#ind_one = np.where(label_train == 1)
#p_one = p_train[ind_one]
#plt.plot(p_zero[:,0], p_zero[:,1],'ro', p_one[:,0],p_one[:,1],'gx')
#plt.grid(True)
#plt.show()


# then we construct the computation graph
X = tf.placeholder(tf.float32, shape=(None, 2), name="X")
y = tf.placeholder(tf.int64, shape=(None), name="label")

n_hidden1 = 30
n_hidden2 = 30
n_outputs = 2 # 2 classes => 2 outputs

# generate the deep neural network first
# fully connected is a helper functon stitching together several layers
with tf.name_scope("dnn"):#
    hidden1 = fully_connected(X, n_hidden1, scope="hidden1")
    #hidden2 = fully_connected(hidden1, n_hidden2, scope="hidden2")
    logits = fully_connected(hidden1, n_outputs, scope="outputs", activation_fn=None)

with tf.name_scope("loss"):
    xentropy = tf.nn.sparse_softmax_cross_entropy_with_logits( labels=y, logits=logits)
    loss = tf.reduce_mean(xentropy, name="loss")

learning_rate = 0.01
with tf.name_scope("train"):
    optimizer = tf.train.GradientDescentOptimizer(learning_rate)
    training_op = optimizer.minimize(loss)

with tf.name_scope("eval"):
    correct = tf.nn.in_top_k(logits, y, 1)
    accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

init = tf.global_variables_initializer()

# and then we train the network
n_epochs = 500

with tf.Session() as sess:
    init.run()
    for epoch in range(n_epochs):
        sess.run(training_op, feed_dict={X: p_train, y: label_train})
        acc_train = accuracy.eval(feed_dict={X: p_train, y: label_train})
        if(epoch % 10 == 0):
            print(epoch, "train accuracy:", acc_train)

    # now we generate random points and classify them...
    p_test = np.random.uniform(low=-5.0, high=5.0, size=(100,2))
    Z = logits.eval(feed_dict={X: p_test})
    y_pred = np.argmax(Z, axis=1)

    # separate the points into the 2 classes
    ind_zero = np.where(y_pred == 0)
    p_zero = p_test[ind_zero]
    ind_one = np.where(y_pred == 1)
    p_one = p_test[ind_one]
    # for comparison we plot the line separating the two classes
    x = np.linspace(-5,5)
    y = (d - a*x)/b
    plt.plot(p_zero[:,0], p_zero[:,1],'ro', p_one[:,0],p_one[:,1],'gx', x,y,'-k')
    plt.grid(True)
    plt.show()
