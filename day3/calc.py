#print("hello")

# width = int(input("Enter width: "))
# height = int(input("Enter height: "))

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--width', help='Width in pixels', required=True, type=int)
parser.add_argument('--height', help='Height in pixels', required=True, type=int)
# parser.add_argument('--area', help='Area in pixels', required=False, type=int)

args = parser.parse_args()

width = args.width
height = args.height

area = width * height
print(area)