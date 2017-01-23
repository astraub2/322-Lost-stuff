
git clone https://github.com/postgres/postgres.git
cd postgres
git checkout REL9_5_STABLE
./configure --prefix=$1
make
make install 
cd ..
curl -O http://mirrors.gigenet.com/apache//httpd/httpd-2.4.25.tar.gz
gunzip httpd-2.4.25.tar.gz
tar xf httpd-2.4.25.tar
cd httpd-2.4.25
./configure --prefix=$1
make
make install 
