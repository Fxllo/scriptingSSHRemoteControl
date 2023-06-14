import paramiko
import json

def send_ssh_command(ip_address, username, password, command):
    try:
        # Crea un oggetto SSHClient
        client = paramiko.SSHClient()

        # Imposta la politica di aggiunta automatica dei server SSH
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connettiti all'indirizzo IP specificato con nome utente e password
        client.connect(ip_address, username=username, password=password)

        # Esegui il comando remoto
        stdin, stdout, stderr = client.exec_command(command)

        # Leggi l'output del comando remoto
        output = stdout.read().decode('utf-8')

        # Stampa l'output
        print(f'Output del comando remoto:\n{output}')

        # Chiudi la connessione SSH
        client.close()

    except paramiko.AuthenticationException:
        print(f'Errore di autenticazione durante la connessione a {ip_address}.')
    except paramiko.SSHException as ssh_exception:
        print(f'Errore SSH durante la connessione a {ip_address}: {str(ssh_exception)}')
    except Exception as e:
        print(f'Errore generico durante la connessione a {ip_address}: {str(e)}')

# Esempio di utilizzo della funzione send_ssh_command
with open('config.json', 'r') as json_file:
    data = json.load(json_file)

username = data['username']
password = data['password']
ip_address = data['ip_address']
command = data['command']

send_ssh_command(ip_address, username, password, command)
