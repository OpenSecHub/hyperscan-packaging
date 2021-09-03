# CentOS-8

## build rpm package with docker

```bash
./build.sh
```

## build local

```bash
#!/usr/bin/bash

set -ex

HS_VER=5.4.0
yum -y install epel-release libarchive python39
yum -y install ragel make cmake boost-devel gcc-c++

mkdir hs_build
cd hs_build

wget https://github.com/intel/hyperscan/archive/v${HS_VER}.tar.gz
tar xf v${HS_VER}.tar.gz


mkdir build
cd build

cmake -DCMAKE_BUILD_TYPE=MinSizeRel   \
      -DBUILD_STATIC_AND_SHARED=on    \
          ../hyperscan-${HS_VER}


make -j`nproc`

# make install
```
