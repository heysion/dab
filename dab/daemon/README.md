# test run
mkdir runenv

virtulenv runenv

sudo su

source runenv/bin/active

python setup.py install

python dabdaemon start -c ../../etc/daemon.conf

