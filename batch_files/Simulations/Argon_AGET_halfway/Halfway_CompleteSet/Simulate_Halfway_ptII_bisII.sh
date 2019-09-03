#!/bin/bash
position=("TopCentre" "BottomCentre")

for pos in "${position[@]}"
do
	for (( i=1; i<=250; i++ ))
	do
		python temp_RESTsimfile_creation.py 100000 Th228 Cap $pos $i
		restfile="$iso"'FromCap'"$pos"'_halfway_'"$i"'temp.rml'
		restG4 $restfile
		rm $restfile
	done
done