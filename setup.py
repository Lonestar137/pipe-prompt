from setuptools import setup, find_packages
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pipe-prompt',
    version='0.01',
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=[
        'prompt_toolkit>=3.0.36',
        'protobuf>=4.21.12',
        'python_editor>=1.0.4',
        'setuptools>=63.2.0',
    ],
    entry_points={
        'console_scripts': [
            'pipe-prompt=pipeprompt.src.main:main'
        ]
    },
    author='Garrett Jones',
    author_email='jonesgc137@gmail.com',
    description='Creates an interactive menu from standard input',
    url='https://github.com/Lonestar137/pipe-prompt',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,
    # package_data={'': ["*json/*", "*cache/sample"]}
)
