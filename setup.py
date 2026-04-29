import subprocess
from setuptools import setup, find_packages
from setuptools.command.build import build
import os
from pathlib import Path


class CustomBuild(build):
    def run(self):
        env = os.environ.copy()
        path = Path(self.build_lib) / "rustoff" / "generated"
        path.mkdir(parents=True, exist_ok=True)
        env["RUSTUP_HOME"] = path
        subprocess.run(
            ["rustup", "toolchain", "install", "1.95.0", "--profile=minimal", "--component=rustfmt"], env=env, check=True
        )
        subprocess.run(
            ["rustup", "+1.95.0", "component", "remove", "rust-std"], env=env, check=True
        )
        super().run()


setup(
    name="rustoff",
    version="0.1.0",
    packages=find_packages(),
    cmdclass={
        "build": CustomBuild,
    },
    include_package_data=True,
    package_data={
        "rustoff": ["generated/**/*", "generated/**/.*"],
    },
    entry_points={"console_scripts": ["rustoff = rustoff:main"]},
)
