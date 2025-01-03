import os.path

from setuptools import setup, find_packages, Extension


root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, "README.md"), "rb") as readme:
    long_description = readme.read().decode("utf-8")


setup(
    name="yyjson",
    packages=find_packages(),
    version="4.0.5",
    description="yyjson bindings for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tyler Kennedy",
    author_email="tk@tkte.ch",
    url="https://github.com/TkTech/py_yyjson",
    keywords=["json", "yyjson"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ],
    license="MIT",
    python_requires=">=3.8",
    extras_require={
        # Dependencies for running tests.
        "test": ["pytest"],
        # Dependencies for package release.
        "release": [
            "sphinx",
            "sphinx-copybutton",
            "ghp-import",
            "bumpversion",
            "black",
            "furo",
        ],
    },
    ext_modules=[
        Extension(
            "cyyjson",
            [
                "yyjson/binding.c",
                "yyjson/memory.c",
                "yyjson/document.c",
                "yyjson/yyjson.c",
            ],
            language="c",
        )
    ],
)
