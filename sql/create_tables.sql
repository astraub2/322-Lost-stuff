
--I made user_pk and logged_in variables for future accesability
--I limeted user name and password to 16 char according
--to specification
--following tables will likely come in handy:
create table users
(user_pk serial primary key,
username varchar(16),
password varchar(16),
active BOOLEAN
logged_in BOOLEAN DEFAULT false);

create table roles
(role_pk serial primary key,
username varchar(255),
active BOOLEAN);

create table user_is
(user_fk INT,
role_fk integer REFERENCES roles (role_pk) not null DEFAULT 1);

-- create table user_supports
-- (user_fk integer REFERENCES users (user_pk) not null DEFAULT 1,
-- facility_fk integer DEFAULT 1);

