from ncclient import manager

HOST = "192.168.56.101"
PORT = 830
USERNAME = "cisco"
PASSWORD = "cisco123!"


def connect_router():
    return manager.connect(
        host=HOST,
        port=PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False,
        look_for_keys=False,
        allow_agent=False
    )