FROM centos:8

# install buildtools and deps
RUN yum -y install epel-release libarchive python39
RUN yum -y install ragel make cmake gcc-c++ zlib-devel bzip2-devel
RUN yum -y install rpm-build redhat-rpm-config rpmdevtools

WORKDIR /

ADD hyperscan.spec /

ADD entrypoint.sh  /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

