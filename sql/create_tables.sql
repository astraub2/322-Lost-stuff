
--I made user_pk and logged_in variables for future accesability
--I limeted user name and password to 16 char according
--to specification
--following tables will likely come in handy:
create table users
(user_pk serial primary key,
username varchar(16),
password varchar(16),
role_fk integer,
active BOOLEAN,
logged_in BOOLEAN);

--roles table connects to users with role_fk
create table roles
(
role_pk serial primary key,
role_name varchar(255));

--returns a table of what each users role is
--may be superfluouse, but keep for now
create table user_is
(user_fk INT,
role_fk integer REFERENCES roles (role_pk),
role_name varchar(255));

create table assets
(assets_pk serial primary key,
 asset_tag varchar(16),
 alt_description varchar(255));

create table facilities
(facilities_pk serial primary key,
fcode varchar(6),
common_name varchar(32),
location varchar(255));

--connects assets and facilities with dates to narrow results and 
--show history of items
create table asset_at
	(asset_fk INT,
		facility_fk integer,
		arrive_dt TIMESTAMP,
		depart_dt TIMESTAMP);

