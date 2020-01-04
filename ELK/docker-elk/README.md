# docker-elk
Basic ELK stack in Docker

Note when running the docker-compose:

- set ``sudo sysctl -w vm.max_map_count=262144``
- set right ports for docker components 
- set right DOCKER_HOST_IP (by looking at ``ifconfig`` in the host machine)
- set the config for docker components 
- creat the kafka topics in the running time 
- set the permission for volume of docker in the host machine (or the docker will exit because of the permission)
- with the components in the same network, we could call services by its name (EX: kafka:9091, zoo:2181,...)