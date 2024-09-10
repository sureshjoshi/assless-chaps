# Trying to make the most trivial, spiritual version of scie-pants

import os
import subprocess
import sys

# ignores PANTS_SOURCE, other envvars, and pants_from_sources

# find_pants_installation -> BUILD_ROOT.find stuff
def get_version() -> str:
    import tomllib
    with open("pants.toml", "rb") as f:
        data = tomllib.load(f)
        version = data["GLOBAL"]["pants_version"]
    return version

def main(argv: list[str]) -> None:
    pid = os.getpid()
    args = argv[1:]
    print(f"{pid}: Launched pants-runner with args: {args}")
    
    if not args:
        version = get_version()
        subprocess.run([f"{os.getcwd()}/pants-runner.scie", "pants", version], check=True)
        sys.exit(0)
    
    version = args[1]
    print(f"{pid}: Attempting to run using version {version}")
    
    # "Download" (e.g. pick) correct scie from local releases and run it (ignoring args)
    subprocess.run([f"{os.getcwd()}/releases/{version}/pants.{version}-cp39-darwin_arm64.scie", "--version"], check=True, env={"SCIE_PANTS_VERSION": "0.12.0"})
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)
