import argparse
import json
import os

from src.utilities import Password


def main(arguments: argparse.Namespace):
    json_file = arguments.jsonfile

    if not os.path.exists(json_file):
        raise FileNotFoundError

    with open(json_file) as f:
        users = json.load(f)

    for user in users:
        password = Password.generate(size=21)
        user['password'] = password

    print(json.dumps(users, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('jsonfile', type=str, help='list of users.')

    main(parser.parse_args())
