# Laboratorio OPCUA-MODBUS 2025 - 2026

## Prerequisiti
- Python > 3.10 
- Powershell (se Windows)

## Clonazione Repo
```
git clone https://github.com/mattiazaccarini/Lab-IoT-OPCUA-Modbus.git
```

## Installazione

### Linux
Navigare nella cartella
```
cd ../Lab-IoT-OPCUA-Modbus/
```
Creare un ambiente virtuale python

```
python3 -m venv env
```

Attivare ambiente virtuale python


```
 source env/bin/activate
```
Installare librerie tramite pip

```
pip install -r requirements.txt
```

### Windows
Navigare nella cartella
```
cd ../Lab-IoT-OPCUA-Modbus/
```
Creare un ambiente virtuale python

```
python -m venv env
```

Attivare ambiente virtuale python


```
 Set-Execution Policy Unrestricted -Scope Process
 env/Scripts/activate
```
Installare librerie tramite pip

```
pip install -r requirements.txt
```
## Esecuzione Esercizio 0
- Aprire due terminali
- Attivare gli ambienti virtuali

Navigare nella cartella
```
cd ../Lab-IoT-OPCUA-Modbus/OPCUA/Esercizio0
```
### Linux
Nel primo terminale eseguire
```
(env) studente@studente:~/Lab-IoT-OPCUA-Modbus/OPCUA/Esercizio0$ python3 server.py
```
Nel secondo terminale eseguire
```
(env) studente@studente:~/Lab-IoT-OPCUA-Modbus/OPCUA/Esercizio0$ python3 client.py
```
### Windows
Nel primo terminale eseguire
```
(env) PS ../Lab-IoT-OPCUA-Modbus/OPCUA/Esercizio0> py server.py
```
Nel secondo terminale eseguire
```
(env) PS ../Lab-IoT-OPCUA-Modbus/OPCUA/Esercizio0> py client.py
```
