import sys
from typing import List
import os
import subprocess

DEBUG=True

def main(argv: List[str] = sys.argv):
    with open("mfiles.txt", "w") as fid:
        for mfile in argv[1:]:
            full_path = os.path.abspath(mfile);
            print(full_path, file=fid)

    with open('run_matlab_smart_indent.m', "w") as fid:
        print(f"""
cd '{os.getcwd()}';
addpath('{os.path.dirname(os.path.realpath(__file__))}');

run('matlab_smart_indent');
exit;
""", file=fid)

    subprocess.run(["matlab", "-wait", "-r", "run_matlab_smart_indent"])

    if not DEBUG:
        os.unlink("mfiles.txt")
        os.unlink("run_matlab_smart_indent.m")

    print(f"argv: {argv}")
    print(f"script path: {os.path.dirname(os.path.realpath(__file__))}")

if __name__ == "__main__":
    main()