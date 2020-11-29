# PingMetrics
**🚧 This project is not ready 🚧**

PingMetrics is a python application that pings to one or more targets and exposes the results in a metrics file. These metrics are read by prometheus. Configuration can be done and results can be seen in an Angular web interface.

## Prerequisits
* Docker
* Docker compose

## Starting
```
git clone https://github.com/JeremyMahieu/PingMetrics.git
cd PingMetrics
docker-compose up
```
## Starting updating
```
git pull
docker-compose up --build
```
## Available endpoints
* Frontend: http://localhost:10504/
* Backend api: http://localhost:10501/api/v1/<route>/
* Metrics: http://localhost:10502/metrics/
* Prometheus: http://localhost:10503/
