#!/bin/bash

sudo docker build -t go-jobrecom .

sudo docker run -p 3050:3050 -it go-jobrecom
