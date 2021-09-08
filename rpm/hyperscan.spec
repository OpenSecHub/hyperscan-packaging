##############################################################################
#                                                                            #
#                           Hyperscan Packaging                              #
#                                                                            #
##############################################################################
Name:           hyperscan
Version:        5.4.0
Release:        2%{?dist}
Summary:        Libraries and header files for the hyperscan library
Group:          Development/Libraries
License:        BSD
URL:            https://www.hyperscan.io/
Vendor:         Intel
BuildArch:      x86_64
ExclusiveArch:  x86_64
Packager:       https://github.com/OpenSecHub/hyperscan-packaging

Source0:        https://github.com/intel/hyperscan/archive/refs/tags/v%{version}.tar.gz
Source1:        http://udomain.dl.sourceforge.net/project/pcre/pcre/8.45/pcre-8.45.tar.gz
Source2:        http://udomain.dl.sourceforge.net/project/boost/boost/1.77.0/boost_1_77_0.tar.gz

BuildRequires:  make,cmake,ragel

AutoReqProv:    no


%description
Hyperscan is a high-performance multiple regex matching library. It
follows the regular expression syntax of the commonly-used libpcre
library, but is a standalone library with its own C API.

Hyperscan uses hybrid automata techniques to allow simultaneous
matching of large numbers (up to tens of thousands) of regular
expressions and for the matching of regular expressions across streams
of data.

Hyperscan is typically used in a DPI library stack.

This package provides the libraries(static and dynamic), include files and
other resources needed for developing Hyperscan applications.


##############################################################################
#                                                                            #
#                             Expand Sources                                 #
#                                                                            #
##############################################################################
%prep
%setup -q -b 1
%setup -q -b 2

##############################################################################
#                                                                            #
#                                   Build                                    #
#     http://intel.github.io/hyperscan/dev-reference/getting_started.html    #
##############################################################################
%build

ln -s ../pcre-8.45             pcre

%if 0%{?el} <8 || 0%{?rhel} < 8
# pcre, CMP0026 policy was introduced in CMake version 3.0, CentOS7 is 2.8.12
sed -i "s/CMAKE_POLICY/#CMAKE_POLICY/g"      pcre/CMakeLists.txt
%endif

mkdir build
cd    build

cmake  -DCMAKE_BUILD_TYPE=RelWithDebInfo  \
       -DBUILD_STATIC_AND_SHARED:BOOL=ON  \
       -DBOOST_ROOT=../boost_1_77_0       \
       -DCMAKE_INSTALL_PREFIX=/usr        \
       -DBUILD_EXAMPLES:BOOL=OFF          \
       -DCMAKE_C_FLAGS=-fPIC              \
       -DCMAKE_CXX_FLAGS=-fPIC            \
       ..

#  FAT-RUNTIME SUPPORT, CentOS7 need GCC(>=8)
#      -DFAT_RUNTIME:BOOL=ON
#      -DBUILD_AVX512VBMI:BOOL=ON


make -j`nproc`

##############################################################################
#                                                                            #
#                                   Install                                  #
#                                                                            #
##############################################################################
%install

cd build
%make_install


##############################################################################
#                                                                            #
#                          Scriptlet Directives                              #
#                                                                            #
##############################################################################
%post

ldconfig >/dev/null 2>&1

%postun

ldconfig >/dev/null 2>&1


%files
##############################################################################
#                                                                            #
#                                   FILES                                    #
#                                                                            #
##############################################################################
/usr/include/hs/*
/usr/lib64/*

%changelog
##############################################################################
#                                                                            #
#                              Change Logs                                   #
#                                                                            #
##############################################################################
* Mon Sep 6 2021 - LubinLew lgbxyz@gmail.com
- build hyperscan-%{version}
