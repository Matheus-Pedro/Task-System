DROP TABLE IF EXISTS completion_status;
DROP TABLE IF EXISTS task;

CREATE TABLE IF NOT EXISTS completion_status (
    id SERIAL PRIMARY KEY,
    title VARCHAR (10) NOT NULL
);

INSERT INTO completion_status (title) VALUES ('started');
INSERT INTO completion_status (title) VALUES ('concluded');
INSERT INTO completion_status (title) VALUES ('forgotten');

CREATE TABLE IF NOT EXISTS task (
    id SERIAL PRIMARY KEY,
    title VARCHAR (50) NOT NULL,
    content TEXT NULL,
    image_content TEXT NULL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    starting_date TIMESTAMP NOT NULL,
    completion_status INTEGER NOT NULL REFERENCES completion_status(id),
);
