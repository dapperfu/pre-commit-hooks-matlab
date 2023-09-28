import sys
from typing import List
import os

def main(argv: List[str] = sys.argv):
    print(os.getcwd())
    print(argv)
    print(os.path.dirname(os.path.realpath(__file__)))

if __name__ == "__main__":
    main()