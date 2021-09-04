# hyperscan-packaging

This package provides the libraries(static and dynamic), include files needed for developing Hyperscan applications.



**Supported distributions and versions**

- [CentOS-7](rpm/el7_x64/)

- [CentOS-8](rpm/el8_x64/)

- Ubuntu - TODO

- Debian - TODO

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
| GCC                                             | >=v4.8.1 | 4.8.5               | 8.4.1    | YES      | -                                    |
| [CMake](http://www.cmake.org/)                  | >=2.8.11 | 2.8.12.2            | 3.18.2   | YES      | -                                    |
| [Ragel](http://www.colm.net/open-source/ragel/) | 6.9      | 7.0.0.9             | 7.0.0.12 | YES      | in epel-release                      |
| [Python](http://www.python.org/)                | 2.7      | 2.7.5               | 3.9.2    | YES      | -                                    |
| [Boost](http://boost.org/)                      | >=1.57   | <mark>1.53.0</mark> | 1.66.0   | YES      | Boost headers required(only headers) |
| [Pcap](http://tcpdump.org/)                     | >=0.8    | 1.5.3               | 1.9.1    | Optional | needed for example code only         |
| [Sqlite](http://www.sqlite.org/)                | >=3.0    | 3.7.17              | 3.26.0   | Optional | for tool `hsbench`                   |
| [Pcre](http://www.pcre.org/)                    | >=8.41   | <mark>8.32</mark>   | 8.42     | Optional | for tool `hscollider`                |

> Note:
> 
> If you want build chimera, place PCRE source directory under Hyperscan root directory, and rename `pcre-8.4x` to `pcre`
> 
> If you want build all tools, install packages`sqlite-devel,pcre-devel,libpcap-devel`
> 
> CentOS7/8 install ragel need install epel repo first (`yum install epel-release`)
> 
> CentOS8 install libpcap-devel need enable PowerTool repo (`/etc/yum.repos.d/CentOS-Linux-PowerTools.repo`)

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
/usr/share/doc/hyperscan/examples/README.md
/usr/share/doc/hyperscan/examples/patbench.cc
/usr/share/doc/hyperscan/examples/pcapscan.cc
```

-----

## Author

Lubin [lgbxyz@gmail.com](mailto:lgbxyz@gmail.com).

## Copyright and License

This module is licensed under the MIT license.

## See Also

- [Hyperscan Developer’s Reference Guide](http://intel.github.io/hyperscan/dev-reference/)
