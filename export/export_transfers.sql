\echo 'asset_tag,request_by,request_dt,approve_by,approve_dt,source,destination,load_dt,unload_dt'



SELECT a.asset_tag, ur.username, r.request_dt, ua.username, r.approve_dt, fs.facility_fcode, fd.fcode, t.load_dt, t.unload_dt FROM 
transfer AS r INNER JOIN users AS ur ON r.requestor_fk=ur.user_pk INNER JOIN transit AS t ON t.transfer_fk=r.transfer_pk INNER JOIN 
users AS ua ON r.approver_fk=ua.user_pk INNER JOIN assets AS a ON r.asset_fk=a.assets_pk INNER JOIN facilities AS fs ON r.source_fk=fs.facilities_pk
INNER JOIN facilities AS fd ON r.destination_fk=fd.facilities_pk;