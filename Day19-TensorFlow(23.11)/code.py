import tensorflow as tf
print(tf.version)
#A tensor is a generalization of vectors and matrices to potentially higher dimensions.

#TENSOR=data+shape
#1. data=float32, int32, string etc
#2. shape=the dimension of data

string=tf.Variable("this is a string", tf.string)
number=tf.Variable(324, tf.int16)
floating=tf.Variable(3.567, tf.float64)

print(string)
print(number)
print(floating)