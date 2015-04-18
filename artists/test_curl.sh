#!/bin/sh

echo "\nRetrieving local server data..."
echo "\nTesting GET call...\n"
curl -i -X GET http://localhost:5000/students/
echo "\n\nDONE"

echo "\nEnter name to post to server:"
read name_input
echo "\nTesting POST call...\n"
curl -H "Content-Type: application/json" -X POST -d '{"name":"'"$name_input"'"}' http://localhost:5000/students/
echo "\n\nDONE"

echo "\nRetrieving newly listed student..."
echo "\nTesting GET call...\n"
curl -i -X Get http://localhost:5000/students/4
echo "\n\nDONE"

echo "\nEnter new name:"
read new_name_input
echo "\nTesting PUT call...\n"
curl -H "Content-Type: application/json" -X PUT -d '{"name":"'"$new_name_input"'"}' http://localhost:5000/students/4
echo "\n\nDONE"

echo "\nName changed from $name_input to $new_name_input"

