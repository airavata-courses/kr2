#!/bin/bash

sudo docker build -t go-job-rec .

sudo docker run -p 3050:3050 -it go-job-rec
