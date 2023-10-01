#!/bin/bash
#all list allowed of HTTP
curl -sI "$1" | grep "Allow" | cut -d " " -f 2- 
