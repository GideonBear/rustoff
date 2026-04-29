from pathlib import Path
import os


if __name__ == "__main__":
    env = os.environ.copy()
    path = Path(__file__).parent / "generated"
    env["RUSTUP_HOME"] = path
    os.execve(
        path / "toolchains/1.95.0-x86_64-unknown-linux-gnu/bin/cargo", ["cargo", "fmt"], env
    )
