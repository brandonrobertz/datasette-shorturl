from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_plugin_is_installed():
    datasette = Datasette(memory=True, metadata={
        "plugins": {
            "datasette-shorturl": {
                "database_path": "./test-shorturls.db"
            }
        }
    })
    response = await datasette.client.get("/-/plugins.json")
    assert response.status_code == 200
    installed_plugins = {p["name"] for p in response.json()}
    assert "datasette-shorturl" in installed_plugins
