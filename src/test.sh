cd ..
rm -r wsgi
mkdir wsgi
cd 322-Lost-stuff
git pull
sh preflight.sh lost 
cd ../wsgi
python app.py 
