import subprocess


ALLOWED_COMMANDS = {
    "pytest",
    "python",
}


def run_command(command: str):

    executable = command.split()[0]

    if executable not in ALLOWED_COMMANDS:
        raise ValueError(
            f"Command not allowed: {executable}"
        )

    result = subprocess.run(
        command,
        shell=True,
        cwd="./workspace",
        capture_output=True,
        text=True,
        timeout=60
    )

    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }

#never give an llm unrestricted access to the shell. Only allow a curated list of commands.