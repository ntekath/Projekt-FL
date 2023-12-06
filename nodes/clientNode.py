import flwr as fl
from nodes import clientModel

clientModel = clientModel()

class MyFlowerClient(fl.client.NumPyClient):
    def __init__(self, model, train_data_path):
        self.model = model
        self.train_data_path = train_data_path

    def get_parameters(self):
        return self.model.get_parameters()

    def fit(self, parameters, config):
        self.model.train(parameters, self.train_data_path)

    def evaluate(self, parameters, config):
        pass

    def predict(self, parameters, data):
        return self.model.predict(parameters, data)

# Beispiel: Flower-Client starten
train_data_path = "C:/Users/noelt/OneDrive/Desktop/Studium/PraxisProjekt/Datensatz/archive/Train_data.csv"
fl.client.start_numpy_client("localhost:8080", client=MyFlowerClient(clientModel, train_data_path))
