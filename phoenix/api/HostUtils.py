import socket

# Default Phoenix server port
PHOENIX_SERVER_PORT = 1250


def isHostAlive(host: str) -> bool:
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return not sock.connect_ex((host, PHOENIX_SERVER_PORT))


def getRobotHost(team: int) -> str:

    # Parse out FRC team id
    te, am = str(team / 100).split(".")

    # Create a list of possible hosts
    possible_hosts = [
        "localhost",                 # Local debug server
        "172.22.11.2",               # RoboRIO connected over USB
        f"10.{te}.{am}.2",           # RoboRIO connected over FRC network
        f"roborio-{team}-frc.local"  # RoboRIO over mDNS
    ]
    
    # Check each host if it is hosting a phoenix server
    for host in possible_hosts:
        if isHostAlive(host):
            return host
    
    return ""
