package com.jobinterest.jobInterest;

import java.util.Arrays;
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
	
	public static JSONObject jobInterest = new JSONObject();
	
	public static void main(String[] args) {
		
		SpringApplication.run(JobInterestApplication.class, args);
		
		Properties props = new Properties();
	     props.put("bootstrap.servers", "localhost:9092");
	     props.put("group.id", "test");
	     props.put("enable.auto.commit", "true");
	     props.put("auto.commit.interval.ms", "1000");
	     props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
	     props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
	     KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(props);
	     consumer.subscribe(Arrays.asList("test-topic"));
	     try {
	    	 while (true) {
		         ConsumerRecords<String, String> records = consumer.poll(100);
		         for (ConsumerRecord<String, String> record : records) {
		         System.out.println(record.toString());
		        	 jobInterest.put(record.key(),record.value());
		         //System.out.println(record.value());
		         
		         
		         }
		     }
		
	     } catch(Exception e) {
	    	// LOGGER.error("Exception occurred while consuming messages",e);
	     }finally {
	    	 consumer.close();
	     }
	     
	}
	
	
}

