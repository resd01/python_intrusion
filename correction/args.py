import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--string", help="String to output")
args = parser.parse_args()

if args.string:
    string = args.string
else:
    string = raw_input('string:')

print string

