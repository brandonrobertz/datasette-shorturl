from datasette import hookimpl, Response
from functools import lru_cache
import hashlib
import sqlite3

import sqlite_utils


@lru_cache(maxsize=3)
def get_shorturl_db(datasette):
    plugin_config = datasette.plugin_config("datasette-shorturl")
    try:
        database_path = plugin_config["database_path"]
    except Exception as e:
        database_path = "shorturl.db"
    return sqlite_utils.Database(sqlite3.connect(database_path))


@lru_cache(maxsize=3)
def hash_from_request(request):
    m = hashlib.sha1()
    m.update(bytes(request.full_path, "utf-8"))
    return m.digest().hex()


@hookimpl
def extra_template_vars(request, datasette, view_name):
    """
    Build a short URL for this request page if it doesn't exist.
    NOTE: This does not overwrite! We could introduce a plugin setting
    that overwrites, but I can't think of a use case where this would
    be necessary.
    """
    if not request:
        return {}
    full = request.full_path
    if view_name != "database":
        return {}
    if not full or full == "/":
        return {}
    # skip plugin pages
    if "/-/" in full:
        return {}
    db = get_shorturl_db(datasette)
    if not db:
        return {}
    h = hash_from_request(request)
    short = f"/-/shorturl/{h}"
    db["urls"].insert({
        "hash": h,
        "full": full,
    }, pk="hash", ignore=True)
    return {
        "shorturl": short
    }


async def shorturl_redirect(request, datasette):
    """
    Receive a short URL request and redirect to the actual page
    """
    h = request.url_vars["hash"]
    assert h, "Bad URL"
    db = get_shorturl_db(datasette)
    entry = db["urls"].get(h)
    # NOTE: We can make this permament with kwarg status=301
    return Response.redirect(entry["full"])


@hookimpl
def register_routes():
    return [
        (r"^/-/shorturl/(?P<hash>.*)$", shorturl_redirect)
    ]
