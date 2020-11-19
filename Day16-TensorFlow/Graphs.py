import tensorflow as tf
import numpy as np
import timeit

@tf.function
#a*b
def multiply_fn(a, b):
  return tf.matmul(a, b)

# Create some tensors
a = tf.constant([[0.5, 0.5]])
b = tf.constant([[10.0], [1.0]])

# Check function
print('Multiple a of shape {} with b of shape {}'.format(a.shape, b.shape))
print(multiply_fn(a, b).numpy())
