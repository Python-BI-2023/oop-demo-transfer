from os import path

import confuse

BASE_DIR = path.dirname(path.abspath(__file__))
config = confuse.Configuration("TransferText2DB", __name__)
config.set_file("credentials.yaml")

SOURCE = str(config["source"])
DESTINATION = str(config["destination"])


POSTGRES_DESTINATION_CREDS = {
    "dbname": config["pg_dest"]["dbname"],
    "user": config["pg_dest"]["user"],
    "password": config["pg_dest"]["password"],
    "host": config["pg_dest"]["host"],
    "port": config["pg_dest"]["port"],
}
