FROM python:3.8

# Kopiere die requirements.txt in den Container
COPY requirements.txt /app/

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Installiere die Python-Pakete aus der requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Installiere jaxlib
RUN pip install --no-cache-dir jaxlib==0.3.10

# Installiere Flower
RUN pip install --no-cache-dir flower


# Kopiere den Federated Learning-Anwendungscode in den Container
COPY clientNode.py /app/

# Befehl zum Ausführen von Flower und deinem Anwendungscode
CMD ["flower", "--port=5555", "--broker=redis://broker:6379/0", "--logging=debug", "--debug"]
