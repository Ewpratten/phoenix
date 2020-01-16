import argparse
from .api.APIRequest import makeRequest
import .api.HostUtils

# Handle user args
parser = argparse.ArgumentParser()
parser.add_argument("team", help="FRC team number")

parser.add_argument("action", help="Action to perform", choices=[
    "listall",     # Try to list all connected devices
    "list",        # List all from a device
    "blink",       # Blink a device
    "dumpcfg",     # Dump a device's cfg to the terminal
    "getversion",  # Get a device's version
    "selftest",    # Run a self-test on a device
    "getusage",    # Get CAN bus usage percent
])

parser.add_argument("-d", "--device", help="Device to address",
                    choices=[
                        "srx",
                        "spx",
                        "canif",
                        "pigeon",
                        "ribbonPigeon",
                        "pcm",
                        "pdp",
                    ])

parser.add_argument("-i", "--id", help="Device ID",
                    action="store_true", default=-1)

args = parser.parse_args()

# Debug print args
print(args)

# Determine Robot host IP
robot_host = HostUtils.getRobotHost(int(args.team))

if robot_host:
    print(f"Found Phoenix server running on {robot_host}")
else:
    print("Could not find any Phoenix servers")
    exit(1)

# Handle "list all" requests
if args.action == "listall":
    all_devices = 


# host = ("localhost", 1250)

print(makeRequest(robot_host,  "", 0, "getdevices"))
