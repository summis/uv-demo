# uv demo

This project demonstrates the use of [`uv`](https://docs.astral.sh/uv/) Python project manager.
[old](./old/) and [new](./new/) folders contain identical software project.
The "old" project is managed with traditional tools such as `pyenv` and `pip`.
The "new" project is managed with `uv`.

Neither of the folders demonstrate "the right way" to organize project - they only show one sensible way.


## Demo project

The demo project contains a simple server application and a mock algorithm. The algorithm can be installed a package, while the application is not meant to be installed.

Screenshot of the app

![application ui](ui.jpeg)


## Conclusions


### Benefits

- One can mostly forget the virtual environment - `uv` takes care of it
- Python version updates do not require manual redoing of the setup
- Better performance for package and Python installations
- No need to add `pyenv` (or other similar tool) specific configurations to your system configs
- `uv` maybe helps enforcing clearer structure as your project grows


### Caveats

- As of writing (2025-01-22) uv is still on version 0.5.22 and does not yet have stable API (source: https://docs.astral.sh/uv/reference/policies/versioning/)


### Other

- Instead of using uv workspaces project can be managed equally conveniently separately, each having their own virtual environments and configurations.