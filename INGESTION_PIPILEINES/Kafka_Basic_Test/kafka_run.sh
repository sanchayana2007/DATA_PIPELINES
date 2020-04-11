
#Check the status of Zookeper 
status=$( echo stat | nc 127.1.1.1  2181 | sed -n 's/.*GMT/"Running"/p')
if [ "$status" == "\"Running\"" ];

then
	    echo "Zookepr Running "
else
	        echo "Zookepr is Stopped"
		echo "Trying to run it in background "
	        exec ./kafka_2.12-2.2.0/bin/zookeeper-server-start.sh  kafka_2.12-2.2.0/config/zookeeper.properties  &
		export Zookeeper_pid=$!
		sleep 2
		status=$( echo stat | nc 127.1.1.1  2181 | sed -n 's/.*GMT/"Running"/p')
		if [ "$status" == "\"Running\"" ];

		then
		    echo "Zookepr started"
		    echo "Starting Kafka"
		 exec  ./kafka_2.12-2.2.0/bin/kafka-server-start.sh kafka_2.12-2.2.0/config/server.properties &
		     export Kafka_pid=$!
		     sleep 5

		    echo "Zookeeper_pid=$Zookeeper_pid"
		    echo "Kafka_pid=$Kafka_pid"
		    
		    echo "Create Kafka Topic"
		
		   exec  ./kafka_2.12-2.2.0/bin/kafka-topics.sh --create --zookeeper 127.1.1.1:2181 --replication-factor 1 --partitions 1 --topic 'fast-messages1'



	        else
		    echo "Unable to Start " 
	        fi

fi
