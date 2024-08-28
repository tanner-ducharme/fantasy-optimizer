from setuptools import setup, find_packages

setup(
    name="fantasy-football-optimizer",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "beautifulsoup4",
        "requests",
        "pandas",
        "pyyaml",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "fantasy-optimizer=cli:main",
        ],
    },
)
