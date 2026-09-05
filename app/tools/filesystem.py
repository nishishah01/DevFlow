from pathlib import Path


WORKSPACE = Path("./workspace")


def read_file(path: str) -> str:

    full_path = WORKSPACE / path

    if not full_path.exists():
        raise FileNotFoundError(path)

    return full_path.read_text()


def write_file(
    path: str,
    content: str
):

    full_path = WORKSPACE / path

    full_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    full_path.write_text(content)

    return f"Updated {path}"