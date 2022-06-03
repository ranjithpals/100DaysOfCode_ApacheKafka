**Day #06 of #100DaysOfCode @ApacheKafka**

Today I was able to understand a bit more about Kafka’s features
1.	Brokers
•	A computer, instance, or container running Kafka process
•	Manager Partitions
•	Handle write and read requests
•	Manager replication of partitions
2.	Replication
•	Copies of data for fault tolerance
•	One lead partition and N-1 followers
•	Writes and reads happen to the same leader
•	An invisible process to most developers.
•	Tunable in the Producer
3.	Producers
•	Client application
•	Puts messages into topics
•	Connection pooling
•	Network buffering
•	Partitioning
4.	Consumers
•	Client application
•	Gets message from topics
•	Group of Consumers logically belong to the Consumer Group
•	Messages can be read multiple times with the knowledge of the record’s offset
•	Typically, number of Consumers in a Consumer group is equal or lesser than the number of partitions of a Topic.
•	Two consumers cannot read the same partition of a given Topic.
•	One consumer can read from more than one Partition of a given Topic.

**Day #07 of #100DaysOfCode @ApacheKafka**

Today I was able to read the messages in the topic: poems through a Consumer which was created using a custom code written in Python (consumer.py)

Steps for the following
-	Create a config file which contains details to 
o	Establish default connection to the Kafka Cluster
o	Define the Consumer group and set the message pointer default position on reset.
-	Create a custom script for Consumer
-	Run the consumer script through CLI to view the messages stored in the Topic.

https://developer.confluent.io/learn-kafka/apache-kafka/consumers-hands-on/

Install pip, virtualenv in Unix Environment
https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d
