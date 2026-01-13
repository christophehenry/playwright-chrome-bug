from pathlib import Path

import pytest
from pytest_httpserver import HTTPServer

BASE_DIR = Path(__file__).resolve().parent.parent



@pytest.fixture
def base_dir():
    yield BASE_DIR


@pytest.fixture
def server(httpserver: HTTPServer):
    template_content = ""
    with open(BASE_DIR / "templates/main.html") as f:
        template_content = "\n".join(f.readlines())
    httpserver.expect_request("/").respond_with_data(template_content, mimetype="text/html; charset=UTF-8")
    yield httpserver