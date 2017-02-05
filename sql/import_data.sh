curl https://classes.cs.uoregon.edu//17W/cis322/files/osnap_legacy.tar.gz
tar -xvzf osnap_legacy.tar.gz
mkdir data
initdb -D $HOME/data
pg_ctl -D $HOME/data -l $HOME/logfile start
createdb lost
psql -d lost -a -f create_tables.sql
cd osnap_legacy

python3 ../add_final.py >output.sql
psql -d lost -a -f output.sql
