# Cavio

Side scrolling platformer for Ludum Dare 57 gamejam




## [PLAY HERE](https://kitao.github.io/pyxel/wasm/launcher/?run=LarsDu.Cavio.cavio.app&gamepad=enabled)

## Environment setup

This repo uses [`uv`](https://docs.astral.sh/uv/getting-started/installation) as the package/environment manager. Make sure to install it before proceeding.

The following command will install packages and setup a virtual environment

```bash
# Install packages
uv sync

# Activate virtual enviornment

## Linux/Unix
. .venv/bin/activate

## Windows
. .venv/Scripts/activate
```

# Gameplay

Play the game

```
pyxel run main.py
```


## Developer notes

Edit graphics, tilemaps, and sound

```
pyxel edit cavio/assets/cavio.pyxres
```

### Development environment setup for contributors

Install linters
```
uv sync --group lint
```

Install pre-commit hooks
```
pre-commit install
pre-commit run --all
```

Feel free to fork, or open PRs to this project at will!