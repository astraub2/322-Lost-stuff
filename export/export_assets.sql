\echo 'asset_tag,description,facility,acquired,disposed'
SELECT asset_tag, alt_description, asset_at.facility_fk, \
asset_at.arrive_dt, asset_at.depart_dt FROM assets JOIN \
asset_at ON asset_fk=assets_pk;



SELECT assets.asset_tag, assets.alt_description, facilities.fcode, asset_at.arrive_dt,\
 concat('NULL', assets.disposed_dt) AS disposed_dt FROM assets \
 INNER JOIN asset_at  ON assets.asset_pk=asset_at.asset_fk 
INNER JOIN facilities AS f ON facilities.facilities_pk=asset_at.facility_fk \
WHERE asset_at.arrive_dt=asset_at.intake_dt AND disposed_dt IS NULL;

SELECT assets.asset_tag, assets.alt_description, facilities.fcode, asset_at.arrive_dt\
, assets.disposed_dt FROM assets INNER JOIN asset_at  ON \
assets.asset_pk=asset_at.asset_fk INNER JOIN facilities  ON \
facilities.facilities_pk=asset_at.facility_fk WHERE \
asset_at.arrive_dt=assets.intake_dt \
AND disposed_dt IS NOT NULL;