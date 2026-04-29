from pathlib import Path
import os


def main():
    env = os.environ.copy()
    path = Path(__file__).parent / "generated"
    if not path.exists():
        path = Path(__file__).parent.parent / "build/lib/generated"
    env["RUSTUP_HOME"] = path
    os.execve(
        path / "toolchains/1.95.0-x86_64-unknown-linux-gnu/bin/cargo", ["cargo", "fmt"], env
    )
