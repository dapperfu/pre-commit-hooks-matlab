import sys
from typing import List
import os
import subprocess

DEBUG=True

def main(argv: List[str] = sys.argv):
    with open("models.txt", "w") as fid:
        for mfile in argv[1:]:
            full_path = os.path.abspath(os.getcwd(), mfile);
            print(full_path, file=fid)

    with open('run_close_simulink_subsystems.m', "w") as fid:
        print(f"""
cd '{os.getcwd()}';
""", file=fid)

    subprocess.run(["matlab", "-batch", "run_close_simulink_subsystems"])
    print(argv)
    print(os.path.dirname(os.path.realpath(__file__)))

    if not DEBUG:
        os.unlink("models.txt")
        os.unlink("run_close_simulink_subsystems.m")

if __name__ == "__main__":
    main()