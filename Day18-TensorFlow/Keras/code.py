import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#A Sequential model is appropriate for a plain stack of layers
# where each layer has exactly one input tensor and one output tensor.

# Create 3 layers
model = keras.Sequential(
    [
        layers.Dense(2, activation="relu"),
        layers.Dense(3, activation="relu"),
        layers.Dense(4),
    ]
)
#Its layers are accessible via the layers attribute:

print(model.layers)

# #You can also create a Sequential model incrementally via the add() method:
# model = keras.Sequential()
# model.add(layers.Dense(2, activation="relu"))
# model.add(layers.Dense(3, activation="relu"))
# model.add(layers.Dense(4))
# #Note that there's also a corresponding pop() method to remove layers: a Sequential model behaves very much like a list of layers.
#
# model.pop()
# print(len(model.layers))  # 2

layer = layers.Dense(3)
layer.weights  # Empty

# Call layer on a test input
x = tf.ones((1, 4))
y = layer(x)
layer.weights  # Now it has weights, of shape (4, 3) and (3,)