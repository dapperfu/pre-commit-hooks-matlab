#!/usr/bin/env python
import subprocess
import sys

def run_matlab_script(script_path):
    try:
        # Replace 'matlab' with the actual MATLAB command or path
        subprocess.run(["matlab", "-nodisplay", "-nodesktop", "-r", f"run('{script_path}'); exit;"])
    except Exception as e:
        print(f"Error running MATLAB script: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: pre_commit_hook.py <path_to_matlab_script>")
        sys.exit(1)
    
    tidy_code_script_path = sys.argv[1]
    
    run_matlab_script(tidy_code_script_path)

if __name__ == "__main__":
    main()