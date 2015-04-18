#!/bin/sh

IFS=''

while read line
do
	curl -H "Content-Type: application/json" -X POST -d "$line" http://localhost:5000/artists/

done < EDM.json
