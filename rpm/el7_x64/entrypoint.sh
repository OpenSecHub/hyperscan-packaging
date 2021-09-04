#!/bin/bash

set -ex

mkdir -p /root/rpmbuild/{BUILD,RPMS,SRPMS,SOURCES,SPECS}

cp -f /hyperscan.spec /root/rpmbuild/SPECS/

#echo "192.168.254.21 udomain.dl.sourceforge.net" >> /etc/hosts

spectool -g -R /root/rpmbuild/SPECS/hyperscan.spec

rpmbuild -v -ba /root/rpmbuild/SPECS/hyperscan.spec 2>&1 | tee /root/rpmbuild/build.log


