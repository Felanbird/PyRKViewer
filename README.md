## Mac Notes
* pyinstaller and wxPython require a python built with `enable-framework` 
on. Therefore, one should do
`env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.7.7` and
use that Python installation for building.
* If the text is blurry in the app bundled by `pyinstaller`, one needs to
add an entry in the pyinstaller settings as described
[here](https://stackoverflow.com/a/40676321)

## Documentation
The documentation can be found at: http://pyrkviewer.readthedocs.io/en/latest/

## PyInstaller Build Notes
* Always run `pyinstaller rkviewer.spec` when `rkviewer.spec` is present.
* If somehow `rkviewer.spec` went missing or you want to regenerate the build specs,
run `pyinstaller -F --windowed --add-data ext/Iodine.dll;. main.py` on Windows
or `pyinstaller -F --windowed --add-data ext/Iodine.dll:. main.py` on Linux/Mac
to generate a file named `main.spec`. Note that if a `main.spec` file is already 
present **it will be overwritten**.

## Note on Style
Usually snake_case is used for function names. However, to retain some degree of backwards 
compatibility for wxPython, subclasses of wxPython classes use PascalCase for their methods,
e.g. `Canvas::RegisterAllChildren`.

## TODOs
* BUG: The handle of a reaction may go out of bounds when a node is being moved. Make sure to clip those
values.
* OPTIMIZE: Do not rebuild reaction forms. Instead, keep them all in a dict() and only make the
currently used one visible.
* REFACTOR: Refactor Minimap so that it's a CanvasElement. We also need CanvasElement functions to
accept both a logical_pos and a device_pos as arguments.
* ENHANCEMENT: Add support for multiple net IDs. Currently all net IDs are set to 0 by default.

## Testing
To run all tests, go to project root and run `python -m unittest`.
To run a particular test, run e.g. `python -m unittest test.rkplugin.test_nodes`.

## Profiling
`python -m cProfile -o rkviewer.stat main.py`
