//get the legacy data  using curl, unzip it etc
mkdir data
initdb -D $HOME/data
pg_ctl -D $HOME/data -l $HOME/logfile start
createdb lost_db
psql -d lost_db -a -f create_tables.sql

cd ..
cd ..
curl -O https://classes.cs.uoregon.edu//17W/cis322/files/osnap_legacy.tar.gz
tar -xvzf osnap_legacy.tar.gz
//run the python script
