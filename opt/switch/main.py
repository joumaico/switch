import re
import subprocess
import sys
import tomllib


def main(config: str):
    """Enables or disables input devices based on a configuration file.

    This function reads a configuration file in TOML format and uses its
    contents to enable or disable input devices using the `xinput` command.
    The configuration file should have `ENABLE` and `DISABLE` sections with
    lists of device names.

    Parameters
    ----------
    config (str)
        The path to the configuration file.

    Raises
    ------
    FileNotFoundError
        If the configuration file does not exist.

    tomllib.TOMLDecodeError
        If the configuration file is not valid TOML.

    subprocess.CalledProcessError
        If an `xinput` command fails.
    """
    with open(config, "rb") as f:
        data = tomllib.load(f)

    for item in subprocess.check_output(["xinput"]).decode().split("\n"):
        if (match := re.search(r"id=(\d+)", item)):
            for d in data["ENABLE"]["devices"]:
                if d in item:
                    subprocess.run(["xinput", "enable", match.group(1)])
                    break
            for d in data["DISABLE"]["devices"]:
                if d in item:
                    subprocess.run(["xinput", "disable", match.group(1)])
                    break


if __name__ == "__main__":
    main(sys.argv[1])
