package com.jobinterest.jobInterest;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;

import org.json.simple.JSONObject;

@CrossOrigin(origins = "http://localhost:3000")
@RestController
@RequestMapping("/jobInterest")
public class JobInterestMapper {
	
	JSONObject jobJOSNObject = JobInterestApplication.jobInterest;
	ArrayList<Object> userInterestList;
	
	
	@GetMapping("/{email}")
	public ArrayList getJobInterest(@PathVariable("email") String email){
		
		userInterestList = new ArrayList();
		String[] a = {"SE","CEO"};
		jobJOSNObject.put("rdasego@iu.edu",a);
		jobJOSNObject.put("karan@iu.edu", "PE");
		jobJOSNObject.put("raghu@iu.edu", "DS");


		
	    for (Object key : jobJOSNObject.keySet()) {

	        String keyStr = (String)key;
	       if(keyStr.equals(email)) 
	        	userInterestList.add((jobJOSNObject.get(keyStr)));
	        	
		
	}	
	    return userInterestList;
}
}
