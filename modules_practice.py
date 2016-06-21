import sys
import os

def List(dir):
    filename = os.listdir(dir)
    print(filename)
def main():
    List(sys.argv[1])
