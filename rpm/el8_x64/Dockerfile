FROM centos:8

RUN yum -y install epel-release libarchive python39
RUN yum -y install ragel make cmake boost-devel gcc-c++
RUN yum -y install rpm-build redhat-rpm-config rpmdevtools

WORKDIR /

ADD hyperscan.spec /

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENV LANG=C.UTF-8

ENTRYPOINT ["/entrypoint.sh"]

