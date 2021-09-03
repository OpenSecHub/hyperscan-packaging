#!/usr/bin/env bash

set -ex

DOCKER=hyperscan_packaging:centos8
CURPATH="$( cd $(dirname $0) ; pwd -P )"

rm   -rf ${CURPATH}/output
mkdir -p ${CURPATH}/output

cp -f ../hyperscan.spec   .
docker build -t ${DOCKER} .
rm -f hyperscan.spec


docker run --rm -t -v ${CURPATH}/output:/root/rpmbuild:Z ${DOCKER}

