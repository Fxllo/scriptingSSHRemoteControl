import paramiko
import json
import re

# 178.20.72.19

def send_ssh_command(ip_address, username, password):
    try:
        # Crea un oggetto SSHClient
        client = paramiko.SSHClient()

        # Imposta la politica di aggiunta automatica dei server SSH
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connettiti all'indirizzo IP specificato con nome utente e password
        client.connect(ip_address, username=username, password=password, port=60022)

        # Esegui il comando remoto
        stdin, stdout, stderr = client.exec_command(command="conf")

        # Leggi l'output del comando remoto
        output = stdout.read().decode('utf-8')
        
        print(f'Output del comando remoto:\n{output}')

        # matches = re.findall(r'add firewall .*', output)
        # matches = [match.replace('\r\r', '') for match in matches]
        
        # acl = re.findall(r"ACL_WAN_BLOCK_ALL_MGMT_IPv4", output)
        # acl = [acl.replace('\r\r', '') for a in acl]
        # for i, match in enumerate(acl, 1):
        #     # print(f"{i}. {match}")
        #     print(f"{i}. {acl}")

        # Chiudi la connessione SSH
        client.close()

    except paramiko.AuthenticationException:
        print(f'Errore di autenticazione durante la connessione a {ip_address}.')
    except paramiko.SSHException as ssh_exception:
        print(f'Errore SSH durante la connessione a {ip_address}: {str(ssh_exception)}')
    except Exception as e:
        print(f'Errore generico durante la connessione a {ip_address}: {str(e)}')

with open('config.json', 'r') as json_file:
    data = json.load(json_file)

username = data['username']
password = data['password']
ip_address = data['ip_address']

send_ssh_command(ip_address, username, password)