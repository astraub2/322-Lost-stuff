
mkdir data
initdb -D $HOME/data
pg_ctl -D $HOME/data -l $HOME/logfile start
createdb lost
psql -d lost -a -f create_tables.sql
cd osnap_legacy

python3 ../add_final.py >output.sql
psql -d lost -a -f output.sql
