# Set base image
FROM zenika/alpine-maven:latest

# Install needed applications
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

RUN mkdir /mfwf
VOLUME /mfwf
WORKDIR /mfwf

ENTRYPOINT ["/bin/bash", "/app/metafacture-runner-4.0.0/flux.sh"]
