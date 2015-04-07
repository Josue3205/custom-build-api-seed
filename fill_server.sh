#!/bin/sh

a=1

#sends a post call to server until the
#variable $a is greater than 30
#posts 30 times

until [ ! $a -lt 31 ]
do
	curl -H "Content-type: application/json" -X POST -d '{"name":"null"}' http://localhost:5000/students/

	a=`expr $a + 1`
done
