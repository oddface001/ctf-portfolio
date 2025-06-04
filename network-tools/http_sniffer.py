from scapy.all import sniff, TCP, Raw
from scapy.layers.inet import IP
import datetime
from termcolor import colored

def process_packet(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load

        try:
            if b"HTTP" in payload or b"GET" in payload or b"POST" in payload:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                src = packet[IP].src
                dst = packet[IP].dst

                print(colored(f"\n[{timestamp}]", "cyan"))
                print(colored(f"[{src} -> {dst}]", "magenta"))

                # Decode payload safely
                try:
                    decoded = payload.decode("utf-8", errors="ignore")
                except:
                    decoded = str(payload)

                lines = decoded.split("\n")
                for line in lines:
                    if line.startswith("GET") or line.startswith("POST"):
                        print(colored(line.strip(), "yellow"))
                    elif line.lower().startswith("host:"):
                        print(colored(line.strip(), "green"))
                    elif line.strip() == "":
                        break
                    else:
                        print(line.strip())

                # Save to file
                with open("http_packets.txt", "a") as f:
                    f.write(f"\n[{timestamp}] {src} -> {dst}\n")
                    f.write(decoded + "\n\n")
        except Exception as e:
            pass  # Avoid crashing on odd payloads

print(colored("Starting enhanced HTTP packet sniffer...\n", "blue"))
sniff(filter="tcp port 80", prn=process_packet, store=0)

