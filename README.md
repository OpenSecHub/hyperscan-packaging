# hyperscan-packaging

This package provides the libraries, include files needed for developing Hyperscan applications.



**Features**

- Support Both static libraries and dynamic libraries

- Support chimera library

- Not Support AVX512/AVX512BMI

**Supported distributions and versions**

- [CentOS-7](rpm/el7_x64/)

- [CentOS-8](rpm/el8_x64/)

- [Ubuntu(hirsute)  - Official](https://packages.ubuntu.com/hirsute/libhyperscan-dev)

- [Debian(bullseye) - Official](https://packages.debian.org/bullseye/libhyperscan-dev)

----

## Libraries

| Name                                                                                                   | Static  | Dynamic     | Remark                                      |
| ------------------------------------------------------------------------------------------------------ | ------- | ----------- | ------------------------------------------- |
| libhs                                                                                                  | Support | Support     | contains both compiler and runtime portions |
| [libhs_runtime](http://intel.github.io/hyperscan/dev-reference/serialization.html#the-runtime-library) | Support | Support     | only contains runtime portions              |
| [chimera](http://intel.github.io/hyperscan/dev-reference/chimera.html)                                 | Support | Not Support | a hybrid of Hyperscan and PCRE              |

----

## Dependency

In addition, the following software is required for compiling the Hyperscan library:

| Dependency                                      | Version  | CentOS7             | CentOS8  | Required | Notes                                |
| ----------------------------------------------- | -------- | ------------------- | -------- | -------- | ------------------------------------ |
| GCC                                             | >=v4.8.1 | 4.8.5               | 8.4.1    | YES      | 4.8.5 not support AVX512(BMI)        |
| [CMake](http://www.cmake.org/)                  | >=2.8.11 | 2.8.12.2            | 3.18.2   | YES      | -                                    |
| [Ragel](http://www.colm.net/open-source/ragel/) | 6.9      | 7.0.0.9             | 7.0.0.12 | YES      | in epel-release                      |
| [Python](http://www.python.org/)                | 2.7      | 2.7.5               | 3.9.2    | YES      | -                                    |
| [Boost](http://boost.org/)                      | >=1.57   | <mark>1.53.0</mark> | 1.66.0   | YES      | Boost headers required(only headers) |
| [Pcap](http://tcpdump.org/)                     | >=0.8    | 1.5.3               | 1.9.1    | Optional | needed for example code only         |
| [Sqlite](http://www.sqlite.org/)                | >=3.0    | 3.7.17              | 3.26.0   | Optional | for tool `hsbench`                   |
| [Pcre](http://www.pcre.org/)                    | >=8.41   | <mark>8.32</mark>   | 8.42     | Optional | for tool `hscollider`                |

> Notes:
> 
> If you want build all tools, install packages`sqlite-devel,pcre-devel,libpcap-devel`
> 
> CentOS7/8 install ragel need install epel repo first (`yum install epel-release`)
> 
> CentOS8 install libpcap-devel need enable PowerTool repo (`/etc/yum.repos.d/CentOS-Linux-PowerTools.repo`)
> 
> CentOS7(GCC-4.8.5) not support AVX512 and AVX512BMI, but CentOS8(GCC-8.4.1) is OK. 
> 
> If you want support AVX512 and AVX512BMI in CentOS7, you need upgrade the GCC(GCC-4.9.2 introduced AVX512 support, AVX512BMI need GCC>=8), you should use [devtoolset](https://access.redhat.com/documentation/en-us/red_hat_developer_toolset/8/pdf/user_guide/red_hat_developer_toolset-10-user_guide-en-us.pdf). but the libstdc++ in devtooset is not compatible with the one in CentOS-7, you should combine libstdc++ to the static library.
> 
> ```bash
> yum install -y centos-release-scl
> yum install -y devtoolset-10-gcc-c++
> scl enable devtoolset-10 bash #source /opt/devtoolset-10/enable
> 
> # build hyperscan
> 
> ar x libhs.a
> ar x libstdc++.a
> ar cru libhs.a *.o
> ranlib libhs.a
> ```

-----

## Third-patry Sources

| Source | Version                                                                                    | Notes               |
| ------ | ------------------------------------------------------------------------------------------ | ------------------- |
| boost  | [1.77.0](http://udomain.dl.sourceforge.net/project/boost/boost/1.77.0/boost_1_77_0.tar.gz) | for all libraries   |
| pcre   | [8.45](http://udomain.dl.sourceforge.net/project/pcre/pcre/8.45/pcre-8.45.tar.gz)          | for chimera library |

> Notes:
> 
> If you want build chimera, place PCRE source directory under Hyperscan root directory, and rename `pcre-8.4x` to `pcre`

-----

## Build Options

> [Hyperscan cmake-configuration](https://intel.github.io/hyperscan/dev-reference/getting_started.html#cmake-configuration)

| Option                  | Defaut         | Build          |
| ----------------------- | -------------- | -------------- |
| CMAKE_BUILD_TYPE        | RelWithDebInfo | RelWithDebInfo |
| BUILD_STATIC_AND_SHARED | OFF            | ON             |
| BOOST_ROOT              | -              | boost_1_77_0   |
| CMAKE_INSTALL_PREFIX    | /usr/local     | /usr           |
| BUILD_EXAMPLES          | ON             | OFF            |
| FAT_RUNTIME             | OFF            | -              |
| BUILD_AVX512            | OFF            | -              |
| BUILD_AVX512VBMI        | OFF            | -              |
| CMAKE_C_FLAGS           | -              | -fPIC          |
| CMAKE_CXX_FLAGS         | -              | -fPIC          |

-----

## File List

```bash
$ rpm -qpl hyperscan-5.4.0-1.el7.x86_64.rpm 
/usr/include/hs/ch.h
/usr/include/hs/ch_common.h
/usr/include/hs/ch_compile.h
/usr/include/hs/ch_runtime.h
/usr/include/hs/hs.h
/usr/include/hs/hs_common.h
/usr/include/hs/hs_compile.h
/usr/include/hs/hs_runtime.h
/usr/lib64/libchimera.a
/usr/lib64/libhs.a
/usr/lib64/libhs.so
/usr/lib64/libhs.so.5
/usr/lib64/libhs.so.5.4.0
/usr/lib64/libhs_runtime.a
/usr/lib64/libhs_runtime.so
/usr/lib64/libhs_runtime.so.5
/usr/lib64/libhs_runtime.so.5.4.0
/usr/lib64/pkgconfig
/usr/lib64/pkgconfig/libch.pc
/usr/lib64/pkgconfig/libhs.pc
```

-----

## Usages

```bash
# libhs and libhs_runtime
$ pkg-config --libs --cflags libhs
-I/usr/include/hs -lhs

# chimera
$ pkg-config --libs --cflags libch
-I/usr/include/hs -lchimera 
```

> Note:
> 
> If you want link the static library to a executable file, you shoud use `-l:libhs.a -lm -lstdc++` format, `-static` or `-Bstatic` options will make a lot of troubles.

-----

## Author

Lubin [lgbxyz@gmail.com](mailto:lgbxyz@gmail.com).

## Copyright and License

This module is licensed under the MIT license.

## See Also

- [Hyperscan Developer’s Reference Guide](http://intel.github.io/hyperscan/dev-reference/)
