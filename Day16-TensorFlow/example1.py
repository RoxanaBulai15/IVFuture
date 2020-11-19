import tensorflow as tf

s = tf.compat.v1.Session()
with tf.compat.v1.get_default_graph().as_default():
  h = tf.constant('Hello, this is TensorFlow')
  print(s.run(h))
  