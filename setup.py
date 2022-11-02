from pathlib import Path

import setuptools

project_dir = Path(__file__).parent

setuptools.setup(
    name="exitstatus",
    version="2.3.0",
    description="POSIX exit status codes",
    long_description=project_dir.joinpath("README.rst").read_text(encoding="utf-8"),
    keywords="exit status POSIX",
    author="John Hagen",
    author_email="johnthagen@gmail.com",
    url="https://github.com/johnthagen/exitstatus",
    packages=["exitstatus"],
    package_data={"exitstatus": ["py.typed"]},
    python_requires=">=3.8",
    zip_safe=False,
    license="MIT",
    license_files=["LICENSE.txt"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
    ],
)
