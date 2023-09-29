import os
import subprocess
import sys
from pathlib import Path
from typing import List


# Debugging.
DEBUG = True
# Setup.
fileList = "models.txt"
moduleDir = os.path.dirname(os.path.realpath(__file__))
moduleScript = Path(__file__).stem
runScript = f"run_{moduleScript}"


def main(argv: List[str] = sys.argv):
    with open(fileList, "w") as fid:
        for mfile in argv[1:]:
            full_path = os.path.abspath(mfile)
            print(full_path, file=fid)

    with open(f"{runScript}.m", "w") as fid:
        print(
            f"""% Autogenerated Run Script.
cd '{os.getcwd()}';
addpath('{moduleDir}');
addpath('{os.path.join(moduleDir, "TidyCode")}');

run('{moduleScript}');
""",
            file=fid,
        )

    if DEBUG:
        status = subprocess.check_output(["matlab", "-logfile", f"{runScript}.log", "-nosplash", "-wait", "-r", runScript])
    else:
        status = subprocess.check_output(["matlab", "-batch", runScript])

    if not DEBUG:
        os.unlink(fileList)
        os.unlink(runScript)

    sys.exit(status)


if __name__ == "__main__":
    main()
