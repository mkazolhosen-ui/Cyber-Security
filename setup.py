from setuptools import setup

setup(
    name="caesar-cipher-cli",
    version="0.1.0",
    description="A CLI tool for Caesar cipher",
    packages=["caesar_cipher"],
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "caesar-cli = cli:main",
        ],
    },
)