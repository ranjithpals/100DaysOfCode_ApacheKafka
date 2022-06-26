
**Day 14 - Added Producer client using Python client file**
(venv) learngvrk@Ranjith-Lenovo:/mnt/c/Users/Owner/Documents/kafka/100DaysOfCode_ApacheKafka/Day06-10$ ./producer.py config.ini\
Produced event to topic purchases: key = jsmith       value = book\
Produced event to topic purchases: key = htanaka      value = book\
Produced event to topic purchases: key = jbernard     value = alarm clock\
Produced event to topic purchases: key = jsmith       value = t-shirts\
Produced event to topic purchases: key = jsmith       value = t-shirts\
Produced event to topic purchases: key = awalther     value = alarm clock\
Produced event to topic purchases: key = sgarcia      value = alarm clock\
Produced event to topic purchases: key = sgarcia      value = batteries\
Produced event to topic purchases: key = htanaka      value = t-shirts\
Produced event to topic purchases: key = eabara       value = t-shirts\

**Run a Producer or Consumer script from CLI (Linux Terminal/WSL)** \
https://developer.confluent.io/learn-kafka/apache-kafka/consumers-hands-on/ \
Ensure that Python 3, pip, and virtualenv are installed on your machine. If they’re not, check out the prerequisites from the getting started with Python guide. \
From a terminal window, activate a new virtual environment and install the confluent-kafka library. \
$ virtualenv env \
$ source env/bin/activate \
$ pip install confluent-kafka \

Determine your cluster endpoint by running: \
$ confluent kafka cluster describe

You need an API key and secret in order to proceed. If you need a new one, make note of the cluster ID that was printed in step 3 and use it to run: \
confluent api-key create --resource {ID} \
Then set the key using: \
confluent api-key use {API Key} --resource {ID} \

Make the script executable and run: \
chmod u+x consumer.py \
./consumer.py config.ini
