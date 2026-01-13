# Minimum reproduceable example for Chrome bug with Playwright 

Using `set_input_files`  multiple times in the same test seems to trigger a JS event only once in Chrome, which 
prevent loading files in multiple operations. This bug reproduces with the [`FileChooser` API](https://playwright.dev/python/docs/api/class-filechooser).
It does not reproduce in Firefox.

## How to run

This MRE uses Python to demonstrate the bug. Install Python and uv. Then run ` uv run pytest` to run the test in Chrome, 
` uv run pytest --browser firefox` to test Firefox.

This example is constituted of a single HTML page with a `<input type="file">` and a JS script intercepting the 
`change` event on that input. When intercepted, the JS script will update the page text with the number of event it 
intercepted and the names of the file selected so far. Then, there's a single pytest test located in `tests/test_input.py`
that aims to test this behavior by calling `set_input_files` on the `<input>` twice. In Chrome, this test will fail 
as the JS script is triggered only once. In Firefox, this test passes.