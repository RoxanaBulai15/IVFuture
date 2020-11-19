import tensorflow as tf

# !!! graphs !!!

# a=(b+c)*(c+2)

#!!! constantele sunt declarate folosind functia tf.constant,
# care primeste ca parametri
# 1. valoarea/variabila
# 2. un string optional

#!!! TensorFlow has many of its own types like tf.float32, tf.int32 etc

# first, create a TensorFlow constant
const = tf.constant(2.0, name="const")
# create TensorFlow variables
b = tf.Variable(2.0, name='b')
c = tf.Variable(1.0, name='c')

@tf.function
def multiply_fn(a, b):
  return tf.matmul(a, b)

def add_fn(a, b):
  return tf.add(a, b)

d = tf.add(b, c, name='d') #d=b+c
e = tf.add(c, const, name='e') #e=c+2.0
# d = add_fn(b, c).numpy() #d=b+c
# e = add_fn(c, const).numpy()  # e=c+2.0
print('Add a of shape {} with b of shape {}'.format(b, c))
print(add_fn(b, c).numpy())
print('Add a of shape {} with b of shape {}'.format(c, const))
print(add_fn(c, const).numpy())
print('Multiple a of shape {} with b of shape {}'.format(d, e))
print(multiply_fn(d, e).numpy())

# # now create some operations
# d = tf.add(b, c, name='d') #d=b+c
# e = tf.add(c, const, name='e') #e=c+2.0
# a = tf.multiply(d, e, name='a') #a=d*e
# #print('Multiple a of shape {} with b of shape {}'.format(a.shape))
# print(a)
# # setup the variable initialisation
# #init_op = tf.global_variables_initializer()
# #init_op=tf.initialize_all_variables()
# init_op=tf.compat.v1.global_variables_initializer()
# #with tf.Session() as sess:
# sess = tf.compat.v1.Session()
# with tf.compat.v1.get_default_graph().as_default():
#     # initialise the variables
#     sess.run(init_op)
#     # compute the output of the graph
#     a_out = sess.run(a)
#     print("Variable a is {}".format(a_out))

