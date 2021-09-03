FROM centos:7

RUN yum -y install epel-release bzip2
RUN yum -y install ragel make cmake gcc-c++
RUN yum -y install rpm-build redhat-rpm-config rpmdevtools

WORKDIR /

# download boost library
RUN curl "https://boostorg.jfrog.io/ui/api/v1/download?repoKey=main&path=release%252F1.77.0%252Fsource%252Fboost_1_77_0.tar.bz2" -L -o boost_1_77_0.tar.bz2
RUN tar xf boost_1_77_0.tar.bz2
RUN rm -f  boost_1_77_0.tar.bz2
RUN mv     boost_1_77_0 boost


ADD hyperscan.spec /

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENV LANG=C.UTF-8

ENTRYPOINT ["/entrypoint.sh"]

