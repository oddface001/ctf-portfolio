from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

# Sniff 10 packets from the network interface
sniff(count=10, prn=packet_callback)

from scapy.all import sniff
from datetime import datetime

LOG_FILE = "captured_packets.txt"

def packet_callback(packet):
    try:
        packet_info = f"[{datetime.now()}] {packet.summary()}"
        print(packet_info)
        with open(LOG_FILE, "a") as log:
            log.write(packet_info + "\n")
    except Exception as e:
        print(f"Error processing packet: {e}")

if __name__ == "__main__":
    print("Starting packet capture... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=False)
