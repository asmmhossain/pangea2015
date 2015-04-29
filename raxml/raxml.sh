#!/bin/bash

for i in {1..4}
do
	for k in "gag" "env"
	do
		raxmlHPC -s Vill\_0$i\_Feb2015_5yr\_$k.muscle.phy -m GTRGAMMAI -n Vill\_0$i\_Feb2015\_5yr\_$k -p 12345
	done
done
