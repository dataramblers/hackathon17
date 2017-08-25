# Set base image
FROM java:8-alpine

ENV VERSION=v8.4.0 \
NPM_VERSION=5 \
YARN_VERSION=latest

# Set up node.js
ENV CONFIG_FLAGS="--fully-static" DEL_PKGS="libstdc++" RM_DIRS=/usr/include

RUN apk add --no-cache --update bash ca-certificates git curl make gcc g++ python linux-headers binutils-gold gnupg libstdc++ && \
  gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    56730D5401028683275BD23C23EFEFE93C4CFFFE && \
  curl -sSLO https://nodejs.org/dist/${VERSION}/node-${VERSION}.tar.xz && \
  curl -sSL https://nodejs.org/dist/${VERSION}/SHASUMS256.txt.asc | gpg --batch --decrypt | \
    grep " node-${VERSION}.tar.xz\$" | sha256sum -c | grep . && \
  tar -xf node-${VERSION}.tar.xz && \
  cd node-${VERSION} && \
  ./configure --prefix=/usr ${CONFIG_FLAGS} && \
  make -j$(getconf _NPROCESSORS_ONLN) && \
  make install && \
  cd / && \
  if [ -z "$CONFIG_FLAGS" ]; then \
    npm install -g npm@${NPM_VERSION} && \
    find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm -rf && \
    if [ -n "$YARN_VERSION" ]; then \
      gpg --keyserver ha.pool.sks-keyservers.net --recv-keys \
        6A010C5166006599AA17F08146C2130DFD2497F5 && \
      curl -sSL -O https://yarnpkg.com/${YARN_VERSION}.tar.gz -O https://yarnpkg.com/${YARN_VERSION}.tar.gz.asc && \
      gpg --batch --verify ${YARN_VERSION}.tar.gz.asc ${YARN_VERSION}.tar.gz && \
      mkdir /usr/local/share/yarn && \
      tar -xf ${YARN_VERSION}.tar.gz -C /usr/local/share/yarn --strip 1 && \
      ln -s /usr/local/share/yarn/bin/yarn /usr/local/bin/ && \
      ln -s /usr/local/share/yarn/bin/yarnpkg /usr/local/bin/ && \
      rm ${YARN_VERSION}.tar.gz*; \
    fi; \
  fi && \
  apk del curl make gcc g++ python linux-headers binutils-gold gnupg ${DEL_PKGS} && \
  rm -rf ${RM_DIRS} /node-${VERSION}* /usr/share/man /tmp/* /var/cache/apk/* \
/root/.npm /root/.node-gyp /root/.gnupg /usr/lib/node_modules/npm/man \
/usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html /usr/lib/node_modules/npm/scripts

# Set up maven
RUN  find /usr/share/ca-certificates/mozilla/ -name "*.crt" -exec keytool -import -trustcacerts \
  -keystore /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/cacerts -storepass changeit -noprompt \
  -file {} -alias {} \; && \
  keytool -list -keystore /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/cacerts --storepass changeit

ENV MAVEN_VERSION 3.5.0
ENV MAVEN_HOME /usr/lib/mvn
ENV PATH $MAVEN_HOME/bin:$PATH

# Ensuring that bower can be run by root (required in the installation step of Zeppelin
RUN echo '{ "allow_root": true }' > /root/.bowerrc

RUN wget http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
mv apache-maven-$MAVEN_VERSION /usr/lib/mvn

ENV Z_VERSION="0.8.0-SNAPSHOT"
ENV LOG_TAG="[ZEPPELIN_${Z_VERSION}]:" \
Z_HOME="/zeppelin" \
LANG=en_US.UTF-8 \
LC_ALL=en_US.UTF-8

# Install Zeppelin
RUN git clone https://github.com/apache/zeppelin.git
WORKDIR ./zeppelin
RUN mvn clean package \
-DskipTests \
-Dbuild-distr \
-Dflink.version=1.3.2 \
-Pspark-2.1 \
-Psparkr \
-Pyarn \
-Phadoop-2.7 \
-Pscala-2.11 \
--projects \
"!groovy,\
!angular,\
!shell,\
!livy,\
!hbase,\
!pig,\
!jdbc,\
!file,\
!ignite,\
!kylin,\
!lens,\
!cassandra,\
!elasticsearch,\
!bigquery,\
!alluxio,\
!scio"

# Tidying up
RUN find bin -type f -name "*.cmd" -exec rm {} \;
RUN rm -r alluxio angular beam bigquery cassandra dev docs elasticsearch file geode groovy hbase helium-dev ignite jdbc kylin lens LICENSE licenses livy NOTICE pig pom.xml r README.md Roadmap.md scalding scio scripts SECURITY-README.md STYLE.md testing _tools travis_check.py zeppelin-examples .git*

ADD * /zeppelin/
VOLUME /zeppelin/notebook

EXPOSE 8080
WORKDIR /zeppelin
RUN chmod +x bin/zeppelin.sh
ENTRYPOINT ["/bin/bash", "bin/zeppelin.sh"]
