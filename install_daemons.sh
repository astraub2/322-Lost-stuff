cd ..
git clone https://github.com/postgres/postres.git
cd postgres
git checkout REL9_5_STABLE
./configure
mkdir build_dir
cd build_dir
cd ..
make
make install DESTDIR=/home/osnapdev

cd ..
curl -O http://mirrors.gigenet.com/apache//httpd/httpd-2.4.25.tar.gz
gunzip httpd-2.4.25.tar.gz
tar xf httpd-2.4.25.tar
cd httpd-2.4.25
./configure
mkdir build_dir
make
make install DESTDIR=/home/osnapdev
