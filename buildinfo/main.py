import argparse
import json
import pprint
import sys

from buildinfo.parse import parse_buildinfo


def main():
    parser = argparse.ArgumentParser(description='.BUILDINFO parser')
    parser.add_argument('--json', action='store_true', help='output JSON')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), default=sys.stdin, help='input file')

    args = parser.parse_args()
    buildinfo = args.file.read()
    data, errors = parse_buildinfo(buildinfo)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(data, indent=4))
    else:
        pprint.PrettyPrinter().pprint(data)
