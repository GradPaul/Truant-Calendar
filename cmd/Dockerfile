FROM    registry.prod.qc.careerdream.com/centos7
MAINTAINER Kaiqiang Xu <a@andyxu.cn>

#       Download or install dependencies
RUN     yum install -y \
        wget \
        make \
        unzip \
        tar \
        gcc-c++ \
        bzip2 \
        giflib-devel \
        giflib \
        gcc \
        libpng \
        libjpeg \
        libpng-devel \
        libjpeg-devel \
        ghostscript \
        libtiff \
        libtiff-devel \
        freetype \
        freetype-devel \
        git \
        zlib-devel \
        bzip2-devel \
        readline-devel \
        sqlite \
        sqlite-devel \
        python-devel  \
        openssl-devel
        

RUN	    curl http://repo.careerdream.org/get-pip.py | python
COPY	./requirements.txt /data/apps/web/etc/requirements.txt
RUN		pip install -r /data/apps/web/etc/requirements.txt

