import flwr as fl
from nodes import clientModel
from server.globalModel import GlobalModel

# Globales Modell
global_model = GlobalModel()

# Flower-Server starten
fl.server.start_server("0.0.0.0:8080", [fl.client.NumPyClient(global_model) for _ in range(3)])

# oder alternativ, wenn Sie spezifische Clients haben
# clients = [
#     MyFlowerClient1(your_local_model),
#     MyFlowerClient2(your_local_model),
#     MyFlowerClient3(your_local_model),
# ]
# fl.server.start_server("0.0.0.0:8080", clients)

# Aggregationsstrategie
def aggregate(parameters_list):
    # Hier sollten Sie die Modellparameter aggregieren, z.B. den Durchschnitt
    aggregated_parameters = sum(parameters_list) / len(parameters_list)
    return aggregated_parameters

# Flower-Server starten und die Aggregationsstrategie festlegen
fl.server.start_server("0.0.0.0:8080", [fl.client.NumPyClient(clientModel) for _ in range(3)], strategy=fl.server.strategy.FedAvg(aggregate))
