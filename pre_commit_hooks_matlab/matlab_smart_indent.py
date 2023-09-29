import os
import subprocess
import sys
from typing import List
from pathlib import Path


# Debugging.
DEBUG = True
# Setup.
fileList = "mfiles.txt"
moduleDir = os.path.dirname(os.path.realpath(__file__))
moduleScript = Path(__file__).stem
runScript = f"run_{moduleScript}.m"


def main(argv: List[str] = sys.argv):
    with open(fileList, "w") as fid:
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
        os.unlink(fileList)
        os.unlink(runScript)

    sys.exit(status)


if __name__ == "__main__":
    main()
