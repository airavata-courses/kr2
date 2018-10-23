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
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.json.simple.JSONObject;

@CrossOrigin
@RestController
@RequestMapping("/jobInterest")
public class JobInterestMapper {
	

	Map<String,ArrayList<String>> jobInetrestMap = JobInterestApplication.jobInterestMap;

	
	
	@GetMapping("/{email}")
	public ArrayList getJobInterest(@PathVariable("email") String email){

		for (String key : jobInetrestMap.keySet()) {
			System.out.println("printing key"+key);
			System.out.println("printing email"+ email);
				if(key.equals(email))
					return jobInetrestMap.get(key);
		}
	
	    return new ArrayList<String>();
}
}
