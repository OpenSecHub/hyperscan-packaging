#!/bin/bash

set -ex

mkdir -p /root/rpmbuild/{BUILD,RPMS,SRPMS,SOURCES,SPECS}

cp -f /hyperscan.spec /root/rpmbuild/SPECS/

spectool -g -R /root/rpmbuild/SPECS/hyperscan.spec

rpmbuild -ba   /root/rpmbuild/SPECS/hyperscan.spec 2>&1 | tee /root/rpmbuild/build.log


