import socket
import netifaces

def scanner_ports():
    #obtenir les informations sur les différents interfaces réseaux dispo sur ma machine
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ips = addresses[netifaces.AF_INET]
            for ip in ips:
                adresse_ip = ip['addr']
                print(f"Interface: {interface}, Adresse IP: {adresse_ip}")
                for port in range(1, 65536):
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(1)
                        result = sock.connect_ex((adresse_ip, port))
                        if result == 0:
                            local_ip, local_port = sock.getsockname()#méthode pour savoir si connexion sur le port
                            if local_ip != '127.0.0.1':
                                print(f"Le port {port} est ouvert et une connexion est établie.")
                                #remote_ip, remote_port = sock.getpeername()(méthode pour obtenir ip connecté sur port ouvert)
                                #print(f"Connexion depuis {remote_ip}:{remote_port}")
                            else:
                                print(f"Le port {port} est ouvert mais aucune connexion n'est établie.")
                        sock.close()
                    except socket.error:
                        print(f"Erreur lors de la connexion au port {port}.")

scanner_ports()