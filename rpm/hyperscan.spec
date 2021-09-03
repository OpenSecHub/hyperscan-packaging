##############################################################################
#                                                                            #
#                           Hyperscan Packaging                              #
# Reference: https://rpm-packaging-guide.github.io/rpm-packaging-guide.pdf   #
#            https://fedoraproject.org/wiki/RPMGroups                        #
#            http://ftp.rpm.org/max-rpm/                                     #
#            https://access.redhat.com/articles/3359321                      #
#                                                                            #
##############################################################################
Name:           hyperscan
Version:        5.4.0
Release:        1%{?dist}
Summary:        Hyperscan is a high-performance multiple regex matching library
Group:          Development/Libraries
License:        BSD
URL:            https://www.hyperscan.io/
Vendor:         Intel
BuildArch:      x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager:       https://github.com/OpenSecHub/hyperscan-packaging

Source0:        https://github.com/intel/hyperscan/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++, make, cmake
AutoReqProv:    no


%description
Hyperscan is a high-performance multiple regex matching library available as 
open source with a C API. Hyperscan uses hybrid automata techniques to allow 
simultaneous matching of large numbers of regular expressions across streams 
of data.

##############################################################################
#                                                                            #
#                           Build and Install                                #
#                                                                            #
##############################################################################
%prep
%setup -q -n "hyperscan-%{version}"


### http://intel.github.io/hyperscan/dev-reference/getting_started.html
%build

%if 0%{?el} >= 8 || 0%{?rhel} >= 8
cmake  -DCMAKE_BUILD_TYPE=RelWithDebInfo        \
       -DBUILD_STATIC_AND_SHARED=on             \
       -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr  \
       .
%else
cmake  -DCMAKE_BUILD_TYPE=RelWithDebInfo        \
       -DBUILD_STATIC_AND_SHARED=on             \
       -DBOOST_ROOT=/boost                      \
       -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr  \
       .
%endif

%{__make} -j`nproc`


%install
%{__make} install

### fix prefix path
sed -i "s#%{buildroot}##g" %{buildroot}/usr/lib64/pkgconfig/libhs.pc
### delete example code
rm -rf %{buildroot}/usr/share

%clean
rm -rf %{buildroot}

##############################################################################
#                                                                            #
#                       Scriptlet Directives                                 #
#                                                                            #
##############################################################################
%post

ldconfig >/dev/null 2>&1


%files
##############################################################################
#                                                                            #
#                                   FILES                                    #
#                                                                            #
##############################################################################
%defattr(-,root,root)
%dir %attr(644,root,root) /usr/include/hs/
%dir %attr(755,root,root) /usr/lib64/
%attr(644,root,root)/usr/include/hs/*
%attr(755,root,root) /usr/lib64/*


%changelog
##############################################################################
#                                                                            #
#                              Change Logs                                   #
#                                                                            #
##############################################################################
* Thu Sep 2 2021 - LubinLew lgbxyz@gmail.com
- build hyperscan-%{version}
