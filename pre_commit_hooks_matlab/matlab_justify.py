import os
import subprocess
import sys
from pathlib import Path
from typing import List

# Debugging.
DEBUG = True
# Setup.
fileList = "mfiles.txt"
moduleDir = os.path.dirname(os.path.realpath(__file__))
moduleScript = {Path(__file__).stem}.m
runScript = f"run_{moduleScript}"


def main(argv: List[str] = sys.argv):
    with open("mfiles.txt", "w") as fid:
        for mfile in argv[1:]:
            full_path = os.path.abspath(mfile)
            print(full_path, file=fid)

    with open(runScript, "w") as fid:
        print(
            f"""
cd '{os.getcwd()}';
addpath('{moduleDir}');
addpath('{os.path.join(moduleDir, "TidyCode")}');

run('{moduleScript}');
quit(1, 'force');
""",
            file=fid,
        )

    if DEBUG:
        status = subprocess.check_output(["matlab", "-wait", "-r", runScript])
    else:
        status = subprocess.check_output(["matlab", "-batch", runScript])

    if not DEBUG:
        os.unlink("mfiles.txt")
        os.unlink(runScript)


if __name__ == "__main__":
    main()
