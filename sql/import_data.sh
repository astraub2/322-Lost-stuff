//get the legacy data  using curl, unzip it etc
mkdir data
initdb -D $HOME/data
pg_ctl -D $HOME/data -l $HOME/logfile start
createdb lost_db
psql -d lost_db -a -f create_tables.sql
path=/osnap_legacy
python3 add_stuff.py