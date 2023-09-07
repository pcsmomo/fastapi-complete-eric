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
- 16-routing
  - `docker compose build && docker compose up`
- 17-alembic
  - the completed version of API!
  - `docker compose build && docker compose up`
  - python backend and PostgreSQL
- 18-fullstack
  - `docker compose build && docker compose up`
  - python backend, static and MySQL

## Details

Run Python in VSCode

1. Ctrl + Command + P : "Python: Run Python File in Terminal"
2. And create a new shortcut Shift + Option + Enter to run it

<details open>
  <summary>Click to Contract/Expend</summary>

## Section 03. Python Installation

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

## Section 7: (renew) Project 1 - FastAPI Request Method Logic

```sh
poetry init
poetry add fastapi uvicorn
```

### 51. Create FastAPI Endpoint

```sh
uvicorn books:app --reload
```

### Postman random name for the body

```json
{
  "title": "{{$randomNoun}}",
  "author": "{{$randomFullName}}",
  "category": "science"
}
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

### 106. FastAPI Project: Hash User Password

```sh
poetry add "passlib[bcrypt]"
```

### 107. FastAPI Project: Save User to Database

```py
models.Base.metadata.create_all(bind=engine)
# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html#accessing-the-metadata
# The declarative_base() base class contains a MetaData object where newly defined Table objects are collected. This object is intended to be accessed directly for MetaData-specific operations. Such as, to issue CREATE statements for all tables:
```

```sh
uvicorn app.auth:app --reload --port 9000

# navigate `http://localhost:8000/docs` and add a user

sqlite3 todos.db
sqlite> select * from users;
```

### 108. FastAPI Project: Authentication of a User

```sh
poetry add python-multipart
```

### 109. FastAPI Project: JSON Web Token (JWT) Creation

```sh
poetry add "python-jose[cryptography]"
```

1. navigate `http://localhost:8000/docs#/default/login_for_access_token_token_post`
2. go to `https://jwt.io/` and check the token we received

### 116. FastAPI Project: Setting up Database with User and Todo Relationships

```sql
-- before this, add two users via the docs page on the web
insert into todos (title, description, priority, complete, owner_id) values ('Take out the dog', 'he needs to use the batnroom', 5, False, 1);
insert into todos (title, description, priority, complete, owner_id) values ('Cut the grass', 'it is get till long', 5, False, 1);
insert into todos (title, description, priority, complete, owner_id) values ('Make dinner', 'kids are home', 5, False, 2);

```

### 117. FastAPI Project: Get Todo (User ID)

```sh
docker compose build && docker compose up
# todo app is on port 8000
# auth service is on port 9000
```

1. get a token from `http://localhost:9000/docs#/default/login_for_access_token_token_post`
2. postman get request to `http://localhost:8000/todos/user`
   - add the token to the 'Authorizaition' -> 'Bearer Token

## Section 10: Authentication & Authorization (renew)

I'd like to go the renewed course with all latest version of packages

- python 3.11
- PyDantic v2

### 97. FastAPI Project: Starting Authentication & Authorization

```sh
python --version
# Python 3.11.3

poetry self update
poetry --version
# Poetry (version 1.5.1)
mv /Users/noah/Library/Preferences/pypoetry/ "/Users/noah/Library/Application Support/pypoetry/"

poetry install
poetry shell
poetry add fastapi
poetry add uvicorn
poetry add sqlalchemy
poetry add autopep8

# python = "^3.10" -> "^3.11"
# fastapi = "^0.87.0" -> "^0.101.0"
# uvicorn = "^0.19.0" -> "^0.23.2"
# sqlalchemy = "^1.4.44" -> "^2.0.19"
# autopep8 = "^2.0.0" -> "^2.0.2"
```

#### Pydantic v1 vs Pydantic v2

- `.dict()` function -> `.model_dump()`
- `schema_extra` function within a `Config` class -> `json_schema_extra`

```sh
poetry shell
uvicorn app.auth:app --reload
```

### 98. FastAPI Project: Routers Scale Authentication File

```sh
poetry shell
uvicorn app.main:app --reload
```

## Section 15. Production Database Setup

### 126. FastAPI Project: PostgreSQL Mac Installation

- [PostgreSQL](https://www.postgresql.org/download/)
  - Or using homebrew
- Tools
  - [pgAdmin4](https://www.pgadmin.org/download/)
  - [postico](https://eggerapps.at/postico2/)
  - [DBeaver](https://dbeaver.io/)

### 127. FastAPI Project: PostgreSQL Create Database Table

### 128. FastAPI Project: PostgreSQL Connect to FastAPI

```sh
poetry add psycopg2-binary
```

### 133. FastAPI Project: Create Database Tables

### 134. FastAPI Project: Connect FastAPI to MySQL

```sh
poetry add pymysql
```

## Section 17. Alembic Data Migration

### Create PostgreSQL database and connect it via docker compose

1. install psycopg2-binary
   ```shm
   poetry add psycopg2-binary
   ```
2. add `postgres` docker image in the `docker-compose.yml`
   - in the `todo-app`, sqlalchemy couln't connect to postgres on m1 mac
   - [`sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SCRAM authentication requires libpq version 10 or above`](https://github.com/psycopg/psycopg2/issues/1360)
   - I had to downgrade to postgres 13 - [reference](https://github.com/ojgenbar/RZDTicketsMonitor/pull/23)
   - and it works!
3. install [DBEAVER - database tool](https://dbeaver.io/)
4. create a database with example credentials (see [`docker-compose.yml`](./17-alembic/docker-compose.yml))
5. create tables and insert some data ([`create_tables.sql`](./17-alembic/db-queries/PostgreSQL/create_tables))
6. sqlalchemy is amazing. `Sqlite` to `PostgreSQL`, no code change at all (except the connection)

### 147. Alembic Introduction

[Alembic Document](https://alembic.sqlalchemy.org/en/latest/)

```sh
poetry add alembic
```

#### Alembic Example

- `alembic init <folder name>`
  - initializes a new, generic environment
- `alembic revision -m <message>`
  - creates a new revision of the environment
- `alembic upgrade <revision #>`
  - run our upgrade migration to our database
- `alembic downgrade <revision #>`
  - run our downgrade migration to our database

#### How does alembic work?

- `alembic.ini` file
  - configuration for alembic
- `alembic` directory
  - has all environmental properties for alembic
  - hold all revisions of the application
  - where we call migrations for upgrading and downgrading

### 148. Alembic Setup

```sh
# ./17-alembic
alembic init alembic
```

In the lecture, he moved all app code to the root \
But I still keep them under app

### 150. Alembic Add New Column

1. modify `alembic.ini` and `alembic/env.py`
2. create a new revision
   ```sh
   poetry shell
   alembic revision -m "create phone number for user col"
   # Generating /Users/noah/Documents/study/study_codes/udemy/fastapi-complete-eric/fastapi-complete-eric-git/17-alembic/alembic/versions/9b73fc7d3375_create_phone_number_for_user_col.py ...  done
   ```
   ```sql
   -- check on the table
   select * from users;
   -- there's no phone number column
   ```
3. add the upgrade script in `alembic/versions/9b73fc7d3375_create_phone_number_for_user_col.py`
   ```sh
   alembic upgrade 9b73fc7d3375
   # INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
   # INFO  [alembic.runtime.migration] Will assume transactional DDL.
   # INFO  [alembic.runtime.migration] Running upgrade  -> 9b73fc7d3375, create phone number for user col
   ```
   ```sql
   -- check on the table
   select * from users;
   -- phone_number column has been created!
   ```
   ```sh
   alembic --help
   ```
4. add the downgrade script in `alembic/versions/9b73fc7d3375_create_phone_number_for_user_col.py`
   ```sh
   alembic downgrade -1
   # INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
   # INFO  [alembic.runtime.migration] Will assume transactional DDL.
   # INFO  [alembic.runtime.migration] Running downgrade 9b73fc7d3375 -> , create phone number for user col
   ```
   ```sh
   # create it back
   alembic upgrade 9b73fc7d3375
   ```

### 151. Alembic Create New Database Table

1. create a new revision
   ```sh
   alembic revision -m "create address table"
   # Generating /Users/noah/Documents/study/study_codes/udemy/fastapi-complete-eric/fastapi-complete-eric-git/17-alembic/alembic/versions/181d687473a4_create_address_table.py ...  done
   ```
2. add upgrade and downgrade scripts
3. execute upgrade
   `alembic upgrade 181d687473a4`
4. create a new revision
   `alembic revision -m "create address_id to users"`
5. add upgrade and downgrade scripts
6. execute upgrade
   `alembic upgrade 4f808f0d858c`

### 155. FastAPI Solution

1. Add a `phone number` as a required field for a user during registration (string).
2. Create a new column on `address`, that is called `apt_num`
3. Enable the application to now use the `apt_num` as an optional field for the address of the user

#### alembic

1. create a new revision
   `alembic revision -m "add apt num col"`
2. add upgrade and downgrade scripts
3. execute upgrade
   `alembic upgrade c511ac47feb4`

## Section 18. Project 4 - Full Stack Application

### Create MySQL database and connect it via docker compose

1. install pymysql
   ```shm
   poetry add pymysql
   ```
2. add `mysql` docker image in the `docker-compose.yml`
3. install [DBEAVER - database tool](https://dbeaver.io/)
4. create a database with example credentials (see [`docker-compose.yml`](./18-fullstack/docker-compose.yml))
5. create tables and insert some data ([`create_tables.sql`](./18-fullstack/db-queries/MySQL/create_tables))
6. modify service to check health (see [`docker-compose.yml`](./18-fullstack/docker-compose.yml))
   - added `healthcheck`
     - even though `depends_on` was added, the `todo-app` couldn't connect mysql at the first time
7. sqlalchemy is amazing. `Sqlite` to `MySQK`, no code change at all (except the connection)

### 160. FastAPI Full Stack - Pip Requirements and Templates

```sh
poetry add aiofiles
poetry add jinja2
```

## Section 20. Deploying FastAPI Applications

### 198. Deployment: Render Introduction

[Render - cloud hosting](https://render.com/)

### 201. Deployment PostgreSQL: Production Database

[ElephantSQL - PostgreSQL hosting](https://www.elephantsql.com/)

</details>
