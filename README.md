# datasette-shorturl

[![PyPI](https://img.shields.io/pypi/v/datasette-shorturl.svg)](https://pypi.org/project/datasette-shorturl/)
[![Changelog](https://img.shields.io/github/v/release/brandonrobertz/datasette-shorturl?include_prereleases&label=changelog)](https://github.com/brandonrobertz/datasette-shorturl/releases)
[![Tests](https://github.com/brandonrobertz/datasette-shorturl/workflows/Test/badge.svg)](https://github.com/brandonrobertz/datasette-shorturl/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/brandonrobertz/datasette-shorturl/blob/main/LICENSE)

A Datasette plugin that provides short URLs for your queries

## Installation

Install this plugin in the same environment as Datasette.

    datasette install https://github.com/brandonrobertz/datasette-shorturl/archive/refs/tags/0.1.0.zip

## Usage

You need to specify a location for the short URLs database. It can be anywhere in your filesystem. So if you want it public, you can place it directly in your `datasette` folder. Or you can put it somewhere else and it won't show up in the databases list. Here's an example of what my `metadata.yml` looks like, for a non-public URLs database:

```
plugins:
  datasette-shorturl:
    database_path: /datasette/secrets/shorturl.db
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-shorturl
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
