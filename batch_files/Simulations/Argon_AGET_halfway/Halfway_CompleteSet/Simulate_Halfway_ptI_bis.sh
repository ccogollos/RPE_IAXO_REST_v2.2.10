#!/bin/bash
isotopes=("Cs137")
component=("Res")
position=("TopCentre" "BottomCentre")

for iso in "${isotopes[@]}"
do
	for comp in "${component[@]}"
	do
		if [ $comp == Cap ]
		then
			for pos in "${position[@]}"
			do
				for (( i=1; i<=250; i++ ))
				do
					python temp_RESTsimfile_creation.py 100000 $iso $comp $pos $i
					restfile="$iso"'From'"$comp""$pos"'_halfway_'"$i"'temp.rml'
					restG4 $restfile
					rm $restfile
				done
			done
		else
			for (( i=1; i<=250; i++ ))
			do
				python temp_RESTsimfile_creation.py 100000 $iso $comp TopCentre $i
				restfile="$iso"'From'"$comp"'TopCentre_halfway_'"$i"'temp.rml'
					restG4 $restfile
					rm $restfile
			done
		fi
	done
done
