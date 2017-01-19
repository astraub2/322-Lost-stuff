create table products
(product_pk INT,
 vendor varchar(255),
 description varchar(255),
 alt_description varchar(255));

create table assets
(assets_pk INT,
 product_fk INT,
 asset_tag varchar(255),
 alt_description varchar(255));

create table vehicles
(vehicle_pk INT,
asset_fk INT);

create table facilities
(facilities_pk INT,
fcode varchar(255),
common_name varchar(255),
location varchar(255));

create table asset_at
	(asset_fk INT,
		facility_fk INT,
		arrive_dt TIMESTAMP,
		depart_dt TIMESTAMP);
create table convoys
	(convoy_pk INT,
		request varchar(255),
		source_fk INT,
		dest_fk INT,
		depart_dt TIMESTAMP,
		arrive_dt TIMESTAMP);
create table used_by
	(vehicle_fk INT,
		convoy_fk INT);
create table asset_on
	(asset_fk INT,
		convoy_fk INT,
		load_dt  TIMESTAMP,
		unload_dt TIMESTAMP);
create table users
(user_pk INT,
username varchar(255),
active BOOLEAN);
create table roles
(role_pk INT,
username varchar(255),
active BOOLEAN);
create table user_is
(user_fk INT,
role_fk INT);
create table user_supports
(user_fk INT,
facility_fk INT);
create table levels
(level_pk INT,
abbrv varchar(255),
comment varchar(255));
create table compartments
(compartment_pk INT,
abbrv varchar(255),
comment varchar(255));
create table security_tags
(tag_pk INT,
level_fk INT,
compartments_fk INT,
user_fk INT,
product_fk, INT,
asset_fk, INT);


