import requests
from .HostUtils import PHOENIX_SERVER_PORT


def makeRequest(addr: str, device: str, id: int, action: str) -> dict:

    # Construct arguments
    args: dict = {
        "model": device,   # Device model
        "id": id,          # Device ID
        "action": action,  # Device action
    }

    # Make API request with constructed args
    response = requests.get(
        f"http://{addr}:{PHOENIX_SERVER_PORT}/", params=args).json()

    return response
