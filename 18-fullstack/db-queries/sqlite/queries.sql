-- CREATE TABLE todos (
-- 	id INTEGER NOT NULL,
-- 	title VARCHAR,
-- 	description VARCHAR,
-- 	priority INTEGER,
-- 	complete BOOLEAN,
-- 	PRIMARY KEY (id)
-- );
-- CREATE INDEX ix_todos_id ON todos (id);

-- insert into todos (title, description, priority, complete) values ('Go to the store', 'Pick up eggs', 5, False);
-- insert into todos (title, description, priority, complete) values ('Cut the lawn', 'Grass is getting long', 3, False);
-- insert into todos (title, description, priority, complete) values ('Feed the dog', 'He is getting hungry', 5, False);

-- DROP TABLE todos;

CREATE TABLE users (
	id INTEGER NOT NULL,
	email VARCHAR,
	username VARCHAR,
	first_name VARCHAR,
	last_name VARCHAR,
	hashed_password VARCHAR,
	is_active BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX ix_users_id ON users (id);
CREATE UNIQUE INDEX ix_users_email ON users (email);
CREATE UNIQUE INDEX ix_users_username ON users (username);
CREATE TABLE todos (
	id INTEGER NOT NULL,
	title VARCHAR,
	description VARCHAR,
	priority INTEGER,
	complete BOOLEAN,
	owner_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(owner_id) REFERENCES users (id)
);
CREATE INDEX ix_todos_id ON todos (id);

insert into todos (title, description, priority, complete, owner_id) values ('Take out the dog', 'he needs to use the batnroom', 5, False, 1);
insert into todos (title, description, priority, complete, owner_id) values ('Cut the grass', 'it is get till long', 5, False, 1);
insert into todos (title, description, priority, complete, owner_id) values ('Make dinner', 'kids are home', 5, False, 2);
