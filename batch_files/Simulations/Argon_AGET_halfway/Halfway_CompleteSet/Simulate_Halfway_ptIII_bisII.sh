#!/bin/bash
component=("Cap" "Res")
position=("TopCentre" "BottomCentre")

for comp in "${component[@]}"
do
	for pos in "${position[@]}"
	do
		for (( i=1; i<=250; i++ ))
		do
			python temp_RESTsimfile_creation.py 100000 U238 $comp $pos $i
			restfile='U238From'"$comp""$pos"'_halfway_'"$i"'temp.rml'
			restG4 $restfile
			rm $restfile
		done
	done
done
