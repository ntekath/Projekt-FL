# clientNode.py

import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
from flower import Client

# Simuliere lokales Modelltraining
def train_local_model(X, y):
    model = tf.keras.Sequential([
        layers.Dense(1, input_shape=(1,))
    ])
    model.compile(optimizer='sgd', loss='mse')
    model.fit(X, y, epochs=5, verbose=0)
    return model

# Simuliere Generierung von Modellaktualisierungen
def generate_model_update(local_model, learning_rate=0.1):
    # Extrahiere Gewichte aus dem lokalen Modell
    local_weights = local_model.get_weights()

    # Führe eine einfache Aktualisierung durch (könnte komplexere Logik sein)
    for i in range(len(local_weights)):
        local_weights[i] = local_weights[i] - learning_rate * np.random.randn(*local_weights[i].shape)

    return local_weights

# Simuliere das Senden von Modellaktualisierungen an den Server
def send_model_update_to_server(model_update):
    # Hier würde die Logik für das Senden des Updates an den Server stehen
    # Zum Beispiel: publish(model_update) für ein MQTT-System oder ähnliches
    pass

# Funktion zur Meldung des Node-Starts
def print_node_started_message():
    print("Client Node gestartet.")

# Verwende Flower-Client
client = Client("tcp://localhost:5555")  # Ändern Sie dies entsprechend Ihrer Flower-Server-Konfiguration

# Hauptausführung
if __name__ == "__main__":

    # Meldung, dass der Node gestartet wurde
    print_node_started_message()

    # Simuliere lokale Daten und Modelltraining
    local_X, local_y = generate_local_data()
    local_model = train_local_model(local_X, local_y)

    # Generiere Modellaktualisierung
    model_update = generate_model_update(local_model)

    # Sende Modellaktualisierung an den Server über Flower
    client.send_model_update(model_update)

    print("Client Node: Modellaktualisierung erfolgreich an den Server gesendet.")
