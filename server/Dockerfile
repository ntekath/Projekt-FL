FROM python:3.8

# Kopiere die Anwendungsdateien (z.B., federated_learning_server.py)
COPY serverNode.py /app/

# Kopiere die requirements.txt und installiere Abhängigkeiten
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Führe den Server-Anwendungscode aus
CMD ["python", "/app/federated_learning_server.py"]
