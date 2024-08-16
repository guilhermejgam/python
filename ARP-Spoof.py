# Tu precisarás scapy e Python

from scapy.all import ARP, send
import time

# Configurações da máquina simulada
simulated_mac = "00:11:22:33:44:55"
simulated_ip = "192.168.3.170"
broadcast_ip = "192.168.3.255"  # Endereço IP de broadcast

# Cria um pacote ARP de resposta (ARP Reply) com broadcast
arp_response = ARP(op=2, hwsrc=simulated_mac, psrc=simulated_ip, hwdst="ff:ff:ff:ff:ff:ff", pdst=broadcast_ip)

# Envia o pacote na rede para simular a presença da máquina
while True:
    send(arp_response, verbose=False)
    print(f"Enviando ARP Reply para broadcast: {simulated_ip} - {simulated_mac}")
    time.sleep(2)  # Espera 2 segundos antes de enviar novamente
