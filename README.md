# datasette-shorturl

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/brandonrobertz/datasette-shorturl/blob/main/LICENSE)

A Datasette plugin that provides short URLs for your queries

![datasette-shorturl provides a header short URL link like in this screenshot](https://github.com/brandonrobertz/datasette-shorturl/blob/main/screenshot.png)

Gives you a header link that takes query URLs that look like this:

`/database?sql=select%0D%0A++count%28em.employer_type%29+*+100+%2F+%28%0D%0A++++select%0D%0A++++++count%28*%29%0D%0A++++from%0D%0A++++++employment+em%0D%0A++++++join+names+n+on+em.name_id+%3D+n.id%0D%0A++++++join+agencies+a+on+em.agency_id+%3D+a.id%0D%0A++++++join+employment+em2+on+em.next_employment_id+%3D+em2.id%0D%0A++++++join+agencies+a2+on+em2.agency_id+%3D+a2.id%0D%0A++++where%0D%0A++++++%28%0D%0A++++++++lower%28a2.agency%29+like+%22%25school%25%22%0D%0A++++++++or+lower%28a2.agency%29+like+%22%25state%22%0D%0A++++++++or+lower%28a2.agency%29+like+%22%25military%25%22%0D%0A++++++++or+lower%28a2.agency%29+like+%22%25deputy%25%22%0D%0A++++++++or+lower%28a2.agency%29+like+%22%25international%25%22%0D%0A++++++%29%0D%0A++++++and+a.id+%21%3D+a2.id%0D%0A++++++and+em.start_date+not+like+%271901%25%27%0D%0A++++++and+em.start_date+is+not+null%0D%0A++%29+as+pct_of_total%2C%0D%0A++em.employer_type%0D%0Afrom%0D%0A++employment+em%0D%0A++join+names+n+on+em.name_id+%3D+n.id%0D%0A++join+agencies+a+on+em.agency_id+%3D+a.id%0D%0A++join+employment+em2+on+em.next_employment_id+%3D+em2.id%0D%0A++join+agencies+a2+on+em2.agency_id+%3D+a2.id%0D%0Awhere%0D%0A++%28%0D%0A++++lower%28a2.agency%29+like+%22%25school%25%22%0D%0A++++or+lower%28a2.agency%29+like+%22%25state%22%0D%0A++++or+lower%28a2.agency%29+like+%22%25military%25%22%0D%0A++++or+lower%28a2.agency%29+like+%22%25deputy%25%22%0D%0A++++or+lower%28a2.agency%29+like+%22%25international%25%22%0D%0A++%29%0D%0A++and+a.id+%21%3D+a2.id%0D%0A++and+em.start_date+not+like+%271901%25%27%0D%0A++and+em.start_date+is+not+null%0D%0Agroup+by%0D%0A++em.employer_type%0D%0Aorder+by%0D%0A++count%28em.employer_type%29+desc`

And turns them into URLs that look like this:

`/-/shorturl/40cc69dd62bc0f75665ca3228dfc9f728a08b693`

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
