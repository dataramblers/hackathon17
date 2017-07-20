# Set base image
# FROM base/archlinux:latest
FROM zenika/alpine-maven:latest

# Refresh package manager
# RUN pacman-db-upgrade
# RUN pacman -Syyu --noconfirm

# Install needed applications
# RUN pacman -S --noconfirm maven jdk8-openjdk
RUN apk add --update curl bash \
&& rm -rf /var/cache/apk/*

WORKDIR /app
ADD . /app

# Install metafacture-runner
RUN curl -L https://github.com/culturegraph/metafacture-runner/releases/download/metafacture-runner-4.0.0/metafacture-runner-4.0.0-dist.tar.gz \
| tar xz
ENV MFRUNNER /app/metafacture-runner-4.0.0


# Install swissbib-extensions
RUN curl -L https://github.com/linked-swissbib/swissbib-metafacture-commands/archive/MF-4.0.tar.gz \
| tar xz
WORKDIR swissbib-metafacture-commands-MF-4.0
RUN mvn clean package shade:shade -Dmaven.test.skip=true
RUN mv ./target/swissbibMF-plugins-1.1.jar ${MFRUNNER}/plugins/
RUN cd .. \
&& rm -r swissbib-metafacture-commands-MF-4.0

# RUN pacman -Rsc --noconfirm maven

RUN mkdir /mfwf
VOLUME /mfwf
WORKDIR /mfwf

ENTRYPOINT ["/bin/bash", "/app/metafacture-runner-4.0.0/flux.sh"]
