import sys
import os
import json


DATA_PATH = "/Users/satyapk/Desktop/git_repos/Algorithms_in_python/StereoSet/data/test_data/dev.json"


def read_data(path):
    with open(path) as f1:
        lines = f1.readlines()
    return json.loads("".join(lines))


def print_keys_in_data(parsed_data):
    print(parsed_data["data"]["intersentence"][0])


def main():
    parsed_file = read_data(DATA_PATH)
    print_keys_in_data(parsed_file)


if __name__ == '__main__':
    main()
