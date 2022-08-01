from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-shorturl",
    description="A Datasette plugin that provides short URLs for your queries",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Brandon Roberts",
    url="https://github.com/brandonrobertz/datasette-shorturl",
    project_urls={
        "Issues": "https://github.com/brandonrobertz/datasette-shorturl/issues",
        "CI": "https://github.com/brandonrobertz/datasette-shorturl/actions",
        "Changelog": "https://github.com/brandonrobertz/datasette-shorturl/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License"
    ],
    version=VERSION,
    packages=["datasette_shorturl"],
    entry_points={"datasette": ["shorturl = datasette_shorturl"]},
    install_requires=["datasette", "sqlite_utils"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    package_data={
        "datasette_shorturl": ["templates/*"]
    },
    python_requires=">=3.7",
)
