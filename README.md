# kafka-Consumer-Producer
build kafka consumer producer using python

### what is Apache kafka ?

Kafka is a distributed system that allows multiple services to communicate with each other via queue based
architecture more details [here](https://kafka.apache.org/documentation/#quickstart).

### Download and install Kafka

with Docker installed you can follow the below steps in order to download the spotify/kafka image on your machine and run image as docker container

- Download spotify/kafka image using docker 
 
 ```bash 
  docker pull spotify/kafka
  ```

- Create docker container using the downloaded image.

``` bash
 docker run -p 2181:2181 -p 9092:9092 --name kafka-docker-container --env ADVERTISED_HOST=127.0.0.1 --env ADVERTISED_PORT=9092 spotify/kafka
  ```


_one nice thing about spotify/kafka docker image it's that it comes with both kafka and zookeeper already configured,
so you don't have to go through all that struggle_ 

### Create kafka topic

to create a topic in kafka broker you can use kafka CLI, open terminal and exec inside kafka container 
```bash
docker exce -it kafka-docker-container bash
```

once you are in the container navigate to this path 

``` bash
cd /opt/kafka_2.11-0.10.1.0/
```

to create a topic run 

``` bash
bin/kafka-topics.sh —-create —-topic first-topic —-zookeeper localhost:2181 —-partitions 1 —-replication-factor 1
```

to list all topics in kafka

``` bash
bin/kafka-topics.sh —-list -—zookeeper localhost:2181
```

### Run Python Scripts

- Create python environment with a name kafka

```bash
python3 -m venv kakfa
```


- Activate kafka environment

``` bash
source kafka/bin/activate
```

- Install requirement in requirement.txt found inside the repo

``` bash
pip install -r requirement.txt
```

- Next we will run producer script to send message to topic

```bash
python3 producer.py
```

 _this script will fetch Bitcoin price vs USD and send it to the topic._
 
- Next we will run the consumer, so we can consumer message from the topic

``` bash 
python3 consumer.py
```

and now you have Kafka cluster, producer and consumer up and running :sunglasses: .

## Authors

- [@ahmedkmadani](https://www.github.com/ahmedkmadani)