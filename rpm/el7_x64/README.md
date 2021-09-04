# CentOS-7

## build rpm package with docker

```bash
./build.sh
```

## build local

```bash
#!/usr/bin/bash

set -ex

HS_VER=5.4.0
BOOST_VER=1.77.0

yum -y install epel-release # for ragel
yum -y install ragel make cmake gcc-c++

mkdir hs_build
cd hs_build

wget https://github.com/intel/hyperscan/archive/v${HS_VER}.tar.gz
tar xf v${HS_VER}.tar.gz

BOOST_FOLDER_NAME=`echo ${BOOST_VER} | sed 's/\./_/g'`
curl "https://boostorg.jfrog.io/ui/api/v1/download?repoKey=main&path=release%252F${BOOST_VER}%252Fsource%252Fboost_${BOOST_FOLDER_NAME}.tar.bz2" -L -o boost-${BOOST_VER}.tar.bz2 || exit 1
tar xf boost-${BOOST_VER}.tar.bz2

mkdir build
cd build

cmake -DCMAKE_BUILD_TYPE=MinSizeRel   \
      -DBUILD_STATIC_AND_SHARED=on    \
      -DBOOST_ROOT=../boost_${BOOST_FOLDER_NAME}  \
          ../hyperscan-${HS_VER}


make -j`nproc`

# make install
```
