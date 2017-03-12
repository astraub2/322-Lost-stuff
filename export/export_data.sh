if [ "$#" -ne 2]; then
    echo "Usage: ./.sh <dbname> <output dir>"
    exit;
fi
#remove directory if it exists
if [-d "$2"]; then
	rm -r $2
#remake directory
fi

mkdir $2

#access database
psql -d $1 -f export_users.sql -t -A  -F "," > $2/users.csv
psql -d $1 -f export_facilities.sql -t -A  -F "," > $2/facilities.csv
psql -d $1 -f export_assets.sql -t -A  -F "," > $2/assets.csv
psql -d $1 -f export_transfers.sql -t -A  -F "," > $2/transfers.csv
