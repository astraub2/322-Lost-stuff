//get the legacy data  using curl, unzip it etc
$HOME
mkdir data
initdb -D data
pq_ctl -D data -l logfile start
createdb lost_db
psql -d lost_dv -a -f create_tables.sql
//psql -d lost_db
//download legacy files
$HOME
curl -O https://classes.cs.uoregon.edu//17W/cis322/files/osnap_legacy.tar.gz
tar -xvzf osnap_legacy.tar.gz
//run the python script
