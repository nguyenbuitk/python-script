import os
import sys
import subprocess
import unshare

def main():
    if len(sys.argv) < 2:
        print("what?")
        sys.exit(1)
    
    if sys.argv[1] == "run":
        run()

def run():
    cmd_args = [sys.executable, __file__, "child"] + sys.argv[2:]
    print(cmd_args)
    try:
        unshare.unshare(unshare.CLONE_NEWUTS | unshare.CLONE_NEWPID)
        # running the subprocess is passed
        result = subprocess.run(cmd_args, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
        result.check_returncode()
    except subprocess.CalledProcessError as e:
        print("Command failed with error: {e}")
        sys.exit(1)
        
def child():
    print(f"Running {sys.argv[2:]} as PID {os.getpid()}")
    
    # Run the command passed as arguments
    try:
        cmd = subprocess.run(sys.argv[2:], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
        cmd.check_returncode()
        
        # Set up chroot
        # os.chroot("/home/rootfs")
        os.chdir("/")
        
        # Mount proc filesystem
        subprocess.run(["mount", "-t", "proc", "proc", "/proc"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        sys.exit(1)
    except OSError as e:
        print(f"OS error: {e}")
        sys.exit(1)

def main():
    if sys.argv[1] == "run":
        run()
    elif sys.argv[1] == "child":
        child()
    else:
        print("what?")
        sys.exit(1)
if __name__ == "__main__":
    main()