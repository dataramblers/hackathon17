# hackathon17
Files and notes about the Swiss Open Cultural Data Hackathon 2017.
For information about the data, use cases, tools, etc, see the Wiki: https://github.com/dataramblers/hackathon17/wiki

## Requirements

### Elasticsearch cluster

* see https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
(especially paragraph on production mode)

* Elasticsearch requires increased virtual memory. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html

### Docker

* Docker CE, most recent version
* recommended: 17.06
* see also hints.md

### Docker Compose

* most recent version
* see also hints.md

## Installation notes

The technical environment runs in Docker containers. This enables everyone to run the infrastructure locally on their computers provided that Docker and Docker Compose are installed.

### How to install Docker and Docker Compose

The package sources of many (Linux-) distributions do not contain the most recent version of Docker, and do not contain Docker Compose at all. You must most likely install them manually.

1. Install Docker CE, preferably 17.06.
* https://docs.docker.com/engine/installation/
* Verify correct installation: `sudo docker run hello-world`
2. Install Docker-Compose.
* https://docs.docker.com/compose/install/
* Check installed version: `docker-compose --version`
3. Clone this repository.
* `git clone git@github.com:dataramblers/hackathon17.git`
4. Increase your virtual memory:
https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html

### How to run the technical environment in Docker (for Linux users)

Use `sudo` for Docker commands.

1. Make sure you have sufficient virtual memory: `sysctl vm.max_map_count` must output at least `262144`.
* To increase the limits for one session:`sudo sysctl -w vm.max_map_count=262144`
* To increase the limits permanently:
	1. Create a new `.conf` file in `/etc/sysctl.d/` (e.g.
`10-vm-max-map-count.conf`, the prefix number just indicating the order in which the
files are parsed)
	2. Add the line `vm.max_map_count=262144` and save the file
	3. Reread values for sysctl: `sudo sysctl -p --system`

2. `cd` to your `hackathon17` directory.
3. `docker-compose up` -> Docker loads the images and initializes the containers
4. Access to the running applications:
* Elasticsearch HTTP: `localhost:9200`
* Elasticsearch TCP: `localhost:9300`
* Zeppelin instance: `localhost:8080`
* Flink RPC: `localhost:6123`
* Dashboard of the Flink cluster: `localhost:8081`
5. If you want to stop and exit the docker containers: `docker-compose down` (in separate terminal) or `Ctrl-c` (in same terminal)

