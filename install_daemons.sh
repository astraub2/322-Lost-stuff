//Appache
curl -o http://mirrors.sonic.net/apache//httpd/httpd-2.4.25.tar.gzcurl
gunzip (thing)
tar xf (thing)
(new dir) Appache
./configure
mkdir build_dir
cd build_dir
cd ..
make
make install DESTDIR=/home/osnapdev

//postgres
git clone https://github.com/postgres/postres.git
cd postgres
git checkout REL9_5_STABLE
./configure
mkdir build_dir
cd build_dir
cd ..
make
make install DESTDIR=/home/osnapdev
