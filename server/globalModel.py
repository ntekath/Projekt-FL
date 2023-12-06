import tensorflow as tf

class GlobalModel(tf.keras.Model):
    def __init__(self):
        super(GlobalModel, self).__init__()
        # Hier können Sie Ihr gewünschtes neuronales Netzwerk definieren
        self.dense1 = tf.keras.layers.Dense(128, activation='relu')
        self.dense2 = tf.keras.layers.Dense(10, activation='softmax')

    def call(self, inputs):
        x = self.dense1(inputs)
        return self.dense2(x)

# Beispiel für die Verwendung des globalen Modells
global_model = GlobalModel()
