package com.jobinterest.jobInterest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.json.simple.JSONObject;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class JobInterestApplication {
	//private static final Logger LOGGER = LoggerFactory.getLogger(JobInterestConsumer.class);
	
	//public static JSONObject jobInterest = new JSONObject();
	
	//public static Map<String,String> jobInterest = new HashMap<>();
	
	public static Map<String,ArrayList<String>> jobInterestMap = new HashMap<String,ArrayList<String>>();
	public static void main(String[] args) {
		
		SpringApplication.run(JobInterestApplication.class, args);
		
		Properties props = new Properties();
	     props.put("bootstrap.servers", "149.165.170.124:9092");
	     props.put("group.id", "my-group");
	     props.put("enable.auto.commit", "true");
	     props.put("auto.commit.interval.ms", "1000");
	     props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
	     props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
	     KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(props);
	     consumer.subscribe(Arrays.asList("sample"));
	     
	     try {
	    	 while (true) {
		         ConsumerRecords<String, String> records = consumer.poll(100);
		         //consumer.seekToBeginning(consumer.assignment());
		         for (ConsumerRecord<String, String> record : records) {
		         System.out.println(record.toString());
		            if(jobInterestMap.containsKey(record.key())) {
		            	ArrayList values = jobInterestMap.get(record.key());
		            	values.add(record.value());
		            	jobInterestMap.put(record.key(),values); 
		            }
		            else {
		            	ArrayList<String> values = new ArrayList<String>();
		            	values.add(record.value());
		            	jobInterestMap.put(record.key(),values); 		            	
		            	
		            }
		         }
		     }
		
	     } catch(Exception e) {
	    	// LOGGER.error("Exception occurred while consuming messages",e);
	     }finally {
	    	 consumer.close();
	     }
	     
	}
	
	
}

