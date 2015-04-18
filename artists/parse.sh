#!/bin/sh

awk 'BEGIN {FS = ","} {if ($0~/^[0-9]*.*/)
				{if ($0~/".*,.*"/) print "error\n"; else print $1"," $2"," $3"," $4"," $5"," $6"," $7"," $8"," $9"," $10"," $11"," $12"," $13"," $14"," $15"," $16 > "EDM.txt"
				}
			}END{print NR}' EDM.csv
