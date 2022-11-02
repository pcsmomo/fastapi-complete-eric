# FastAPI - The Complete Course 2022

FastAPI - The Complete Course 2022 (Beginner + Advanced) by Eric Roby

## Details

Run Python in VSCode

1. Ctrl + Command + P : "Python: Run Python File in Terminal"
2. And create a new shortcut Shift + Option + Enter to run it

<details open>
  <summary>Click to Contract/Expend</summary>

Section 03. Python Installation

### 10. Setup Integrated Development Environment

#### pyenv

brew update
brew install pyenv
pyenv install 3.10.7

#### Poetry setup myself

[Poetry documents](https://python-poetry.org/docs/)

1. Install
   - `curl -sSL https://install.python-poetry.org | python3 -`
2. fix .zshrc
   - Add `export PATH="/Users/noah/.local/bin:$PATH"` to your shell configuration file.
3. Enable tab completion for Bash, Fish, or Zsh
   - ```sh
     mkdir ~/.zfunc
     poetry completions zsh > ~/.zfunc/_poetry
     ```
   - add followings to `~/.zshrc,`
     ```
     fpath+=~/.zfunc
     autoload -Uz compinit && compinit
     ```
4. poetry
   - `poetry new 03-poetry-install`
   - `poetry shell`
   - `python 03-poetry-install/__init__.py`

#### vscode formatter

```sh
# install autopep8
/Users/noah/.pyenv/versions/3.10.7/bin/python -m pip install -U autopep8
# pip update
/Users/noah/.pyenv/versions/3.10.7/bin/python -m pip install --upgrade pip
```

### 13. Download Source Code

```sh
pip install -r requirements.txt
```

</details>
