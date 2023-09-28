import sys
from typing import List
import os
import subprocess

def main(argv: List[str] = sys.argv):
    with open('run_matlab_smart_indent.m', "w") as fid:
        print(f"cd '{os.getcwd()}';", file=fid)

    subprocess.run(["matlab", "-batch", "run_matlab_smart_indent"])
    print(argv)
    print(os.path.dirname(os.path.realpath(__file__)))

if __name__ == "__main__":
    main()