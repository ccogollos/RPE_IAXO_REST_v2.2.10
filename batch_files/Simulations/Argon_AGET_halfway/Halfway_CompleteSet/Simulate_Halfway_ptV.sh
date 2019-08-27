#!/bin/bash
isotopesChip=("Th228" "U238")

for iso in "${isotopesChip[@]}"
do
	for (( i=1; i<=2; i++ ))
	do
		python temp_RESTsimfile_creation.py 100000 $iso Chip None $i
		restfile="$iso"'FromChip_halfway_'"$i"'temp.rml'
		restG4 $restfile
		rm $restfile
	done
done