from playwright.async_api import Page


def test_input(page: Page, server, base_dir):
    page.goto(server.url_for("/"))
    page.locator("#file").set_input_files(f'{base_dir / "static/test1.txt"}')
    assert page.locator("#count").text_content() == "Event called 1 times; files: test1.txt"

    page.locator("#file").set_input_files(f'{base_dir / "static/test1.txt"}')
    assert page.locator("#count").text_content() == "Event called 2 times; files: test1.txt, test1.txt"
