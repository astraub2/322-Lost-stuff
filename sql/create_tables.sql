
--I made user_pk and logged_in variables for future accesability
--I limeted user name and password to 16 char according
--to specificationroles
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
 alt_description varchar(255),
 disposed_dt timestamp DEFAULT NULL);

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
		depart_dt timestamp DEFAULT NULL);

--tracks where the assets are transering
--track requests with a request id
--track who requests, who approves, and time of request and approval
--track source and destination of asset, and asset_fk
create table transfer
	(	transfer_pk serial primary key,
		asset_fk INT,
		requestor_fk INT REFERENCES users (user_pk),
		approver_fk INT REFERENCES users (user_pk) DEFAULT NULL,
		request_dt timestamp DEFAULT NULL,
		approve_dt timestamp DEFAULT NULL,
		source_fk INT,
		destination_fk INT;
--tracks what asset, where its going, and time of load and unload
create table transit
	(	asset_fk INT,
		transfer_fk Int REFERENCES transfer (transfer_pk),
		source_fk INT,
		destination_fk INT,
		load_dt timestamp DEFAULT NULL,
		unload_dt timestamp DEFAULT NULL);
