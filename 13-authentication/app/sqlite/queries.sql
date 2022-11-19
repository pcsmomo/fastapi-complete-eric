CREATE TABLE todos (
	id INTEGER NOT NULL,
	title VARCHAR,
	description VARCHAR,
	priority INTEGER,
	complete BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX ix_todos_id ON todos (id);

insert into todos (title, description, priority, complete) values ('Go to the store', 'Pick up eggs', 5, False);
insert into todos (title, description, priority, complete) values ('Cut the lawn', 'Grass is getting long', 3, False);
insert into todos (title, description, priority, complete) values ('Feed the dog', 'He is getting hungry', 5, False);