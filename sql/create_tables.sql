create table products
(product_pk int,
 vendor varchar(255),
 description varchar(255),
 alt_description varchar(255));

create table assets
(assets_pk int,
 product_fk integer not null DEFAULT 1,
 asset_tag varchar(255),
 alt_description varchar(255));

create table vehicles
(vehicle_pk serial primary key,
asset_fk INT);

create table facilities
(facilities_pk int,
fcode varchar(255),
common_name varchar(255),
location varchar(255));

create table asset_at
	(asset_fk INT,
		facility_fk integer,
		arrive_dt TIMESTAMP,
		depart_dt TIMESTAMP);
create table convoys
	(convoy_pk serial primary key,
		request varchar(255),
		source_fk integer,
		dest_fk integer null DEFAULT 1,
		depart_dt TIMESTAMP,
		arrive_dt TIMESTAMP);
create table used_by
	(vehicle_fk integer REFERENCES vehicles (vehicle_pk) not null DEFAULT 1,
		convoy_fk integer REFERENCES convoys (convoy_pk) not null DEFAULT 1);
create table asset_on
	(asset_fk integer DEFAULT 1,
		convoy_fk integer REFERENCES convoys (convoy_pk) not null DEFAULT 1,
		load_dt  TIMESTAMP,
		unload_dt TIMESTAMP);
create table users
(user_pk serial primary key,
username varchar(255),
active BOOLEAN);
create table roles
(role_pk serial primary key,
username varchar(255),
active BOOLEAN);
create table user_is
(user_fk INT,
role_fk integer REFERENCES roles (role_pk) not null DEFAULT 1);
create table user_supports
(user_fk integer REFERENCES users (user_pk) not null DEFAULT 1,
facility_fk integer DEFAULT 1);
create table levels
(level_pk serial primary key,
abbrv varchar(255),
comment varchar(255));
create table compartments
(compartment_pk integer,
abbrv varchar(255),
comment varchar(255));

create table security_tags
(tag_pk serial primary key,
level_fk integer REFERENCES levels (level_pk) not null DEFAULT 1,
compartments_fk integer not null DEFAULT 1,
user_fk integer REFERENCES users (user_pk) not null DEFAULT 1,
product_fk integer REFERENCES products (product_pk) not null DEFAULT 1,
asset_fk integer REFERENCES assets (asset_pk) not null DEFAULT 1);


