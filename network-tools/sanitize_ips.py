import socket
import re

def get_local_ip():
    """Return the local IP address of the current machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return None

def sanitize_file(input_file, output_file, additional_ips=None):
    """Replace sensitive IPs in a file with placeholders."""
    try:
        with open(input_file, "r") as f:
            content = f.read()

        local_ip = get_local_ip()
        if local_ip:
            content = content.replace(local_ip, "<YOUR_LOCAL_IP>")

        if additional_ips:
            for ip in additional_ips:
                content = content.replace(ip, "<REDACTED_IP>")

        # Optional: redact all IPv4 addresses (comment if not needed)
        # content = re.sub(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", "<IP>", content)

        with open(output_file, "w") as f:
            f.write(content)

        print(f"Sanitized output saved to {output_file}")
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Change these as needed
    input_log = "captured_packets.txt"
    output_log = "redacted_packets.txt"

    # Optional: list any public IPs you want to redact too
    custom_ips_to_hide = [
        # "41.x.x.x",  # replace with your public IP if known
    ]

    sanitize_file(input_log, output_log, custom_ips_to_hide)
