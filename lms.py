from NetworkManager import NetworkManager
import json
from DBManager import DBManager

def main():
    network = NetworkManager()
    json_string = network.getPresence()
    seats = json.loads(json_string)

    db_manager = DBManager()
    for item in seats:
        db_manager.create_seat(item)


if __name__ == '__main__':
    main()