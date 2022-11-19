# FastAPI - The Complete Course 2022

FastAPI - The Complete Course 2022 (Beginner + Advanced) by Eric Roby

## Folder structure

- 06-virtual-env
  - books : only env
- 07-fastapi-basic
  - books.py : basic routes
  - examples.py : examples
- 08-fastapi-advanced
  - books2.py
    - pydantic: Data validation(typing)
- 09-http-exceptions-status-code
  - books2.py
- 11-database (until section 12 api-request-methods)
  - app : Todo App
    ```sh
    uvicorn app.main:app --reload
    # or
    docker compose build && docker compose up
    ```
    - create user service
    ```sh
    uvicorn app.auth:app --reload
    ```

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

[VSCode Python formatting](https://code.visualstudio.com/docs/python/editing#_formatting)

- `settings.json` in vscode
  ```json
  {
    "[python]": {
      "editor.defaultFormatter": null,
      "editor.tabSize": 4,
      "editor.formatOnSave": true
    },
    "python.formatting.provider": "autopep8"
  }
  ```
- add `.pep8`
  ```yaml
  [pycodestyle]
  max_line_length = 120
  ignore = "E501,W6"  # or ["E501", "W6"]
  recursive = true
  aggressive = 1
  ```

#### import (report Missing Imports)

```sh
poetry shell
# Spawning shell within /Users/noah/Library/Caches/pypoetry/virtualenvs/virtual-env-BQA6ArIp-py3.10
```

```json
// settings.json
{
  "python.defaultInterpreterPath": "/Users/noah/Library/Caches/pypoetry/virtualenvs/virtual-env-BQA6ArIp-py3.10/bin/python",
  "python.analysis.extraPaths": ["app", "another/path/etc"]
}
```

### 13. Download Source Code

```sh
pip install -r requirements.txt
```

### 46. FastAPI and VirtualENV Installation (Mac)

```sh
# However, I'm going to use poetry instead of venv
pip3 install virtualenv
python3 -m venv fastapienv
. fastapienv/bin/activate
deactivate
```

```sh
poetry init
poetry add fastapi
poetry add uvicorn
uvicorn books:app --reload
# navigate localhost:8000
```

### 47. FastAPI Project: Swagger, HTTP Request Methods, and Status Codes Overview

[OpenAPI Specification](https://swagger.io/specification/)

- http://localhost:8000/openapi.json
- http://localhost:8000/docs

FastAPI Response Status Code

- 1XX - Informational Response: Request processing
- 2XX - Success: Request successfully complete
- 3XX - Redirection: Further action must be complete
- 4XX - Client Errors: An error was caused by the request from the clinent
- 5XX - Server Errors: An error has occurred on the server

## Section 07. Project 1 - FastAPI Request Method Logic

### 53. FastAPI Project: Enhance Get Request

```sh
source /Users/noah/Library/Caches/pypoetry/virtualenvs/virtual-env-BQA6ArIp-py3.10/bin/activate

poetry init
poetry add fastapi uvicorn

poetry shell
# source /Users/noah/Library/Caches/pypoetry/virtualenvs/07-fastapi-basic-G7qb60mq-py3.10/bin/activate
uvicorn books:app --reload
# navigate localhost:8000
```

### 54. FastAPI Project: Path Parameters

> To take the dynamic path parameter properly, the route for dynamic path, \
> `{{book_id}}` should be stated below the static router `mybook`

```py
@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "My favorite book"}

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_title": book_id}
```

## Section 08. Project 2 - Move Fast with FastAPI

### 64. Books 2 Project Overview

```sh
poetry init
poetry add fastapi uvicorn

poetry shell
# /Users/noah/Library/Caches/pypoetry/virtualenvs/08-fastapi-advanced-wumQm9a7-py3.10
source /Users/noah/Library/Caches/pypoetry/virtualenvs/08-fastapi-advanced-wumQm9a7-py3.10/bin/activate

uvicorn books2:app --reload
# navigate localhost:8000
```

### 81. FastAPI Project: Form Fields

```sh
# RuntimeError: Form data requires "python-multipart" to be installed.
# You can install "python-multipart" with:
poetry add python-multipart
```

## Section 11. Setup Database

### 88. FastAPI Project: Database Connection with ORM SQLAlchemy

```sh
mkdir 11-database && cd 11-database
poetry init
poetry add fastapi uvicorn autopep8
poetry add sqlalchemy
```

### 90. FastAPI Project: Main (Create Database Connection for API)

```sh
# 11-database
uvicorn app.main:app --reload
```

```sh
# set up for docker compose
docker compose build && docker compose up
```

### 92. FastAPI Project: Installation of SQLite3 Terminal (Mac)

```sh
# 11-database
brew install sqlite
```

### 94. FastAPI Project: SQLite3 Setting Up Todos

```sh
sqlite3 todos.db
sqlite> .schema
```

```sql
sqlite> insert into todos (title, description, priority, complete) values ('Go to the store', 'Pick up eggs', 5, False);
sqlite> insert into todos (title, description, priority, complete) values ('Cut the lawn', 'Grass is getting long', 3, False);
sqlite> insert into todos (title, description, priority, complete) values ('Feed the dog', 'He is getting hungry', 5, False);
sqlite> select * from todos;

sqlite> .mode column
sqlite> select * from todos;

sqlite> .mode markdown
sqlite> select * from todos;

sqlite> .mode box
sqlite> select * from todos;

sqlite> .mode table
sqlite> select * from todos;

sqlite> insert into todos (title, description, priority, complete) values ('Test element', 'He is getting hungry', 5, False);
sqlite> delete from todos where id = 4;
sqlite> insert into todos (title, description, priority, complete) values ('A new test element', 'He is getting hungry', 5, False);
sqlite> select * from todos;
sqlite> delete from todos where id = 4;

sqlite> .help
sqlite> .exit
```

## Section 13. Authentication & Authorization

### 101. JSON Web Token (JWT) Overview

JWT(Json Web Token) Structure

**aaaaaaaa.bbbbbbbb.cccccccc**

1. Header: (a)
   - alg: The algorithm for signing
   - typ: The specific type of token
   ```json
   {
     "alg": "HS256",
     "typ": "JWT"
   }
   ```
   - The JWT header is then encoded using Base64 to create the first part of the JWT (a)
2. Payload: (b)
   - A JWT Paylaod consists of the data. The payloads data contains claims, and there are three different types of claims
     - Registered
     - Public
     - Private
     ```json
     {
       "sub": "1234567890",
       "name": "Noah Kim",
       "given_name": "Noah",
       "family_name": "Kim"
     }
     ```
   - The JWT payload is then encoded using Base64 to create the first part of the JWT (b)
3. Signature: (c)
   - A JWT Signature is created by using the algorithm in the header to hash out the encoded header, encoded payload with a secret
   - The secret can be anything, but it saves somewhere on the server that the client does not have access to
   - The signature is the thrid and final part of the JWT (c)
   ```js
   HMACSHA256(
     base64UrlEncode(header) + "." + base64UrlEncode(payload),
     your - 256 - bit - secret
   );
   ```

[jwt.io](https://jwt.io/)

### 104. FastAPI Project: Create Database Table for Users

```sql
DROP TABLE todos;
```

### 105. FastAPI Project: Create Authentication & Post Request

```sh
uvicorn app.auth:app --reload
```

</details>
