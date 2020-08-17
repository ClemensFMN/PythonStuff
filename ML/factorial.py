import tensorflow as tf

# we want to calculate the factorial
# the value n
n = tf.Variable(1, name="n")
# and some kind of accumulator storing what we have multiplied so far
acc = tf.Variable(1, name="Acc")

# define the "new value"
fct = n*acc

# update the accumulator with the new value
update_op_1 = tf.assign(acc, fct)
# increase n
update_op_2 = tf.assign(n, n+1)


# init all variables
init = tf.global_variables_initializer()

# computation graph is finished, now obtain a session
with tf.Session() as sess:
    sess.run(init) # init
    print(fct.eval())
    for nval in range(1, 5):
        # we need to run both update operations
        sess.run(update_op_1)
        print("nval = " , nval, " , n = ", n.eval(), " fct = ", fct.eval())
        sess.run(update_op_2)
        print("nval = " , nval, " , n = ", n.eval(), " fct = ", fct.eval())



