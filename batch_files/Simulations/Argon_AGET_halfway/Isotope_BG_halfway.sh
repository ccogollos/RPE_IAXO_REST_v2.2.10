#!bin/bash
export IAXOD0_GEODIR='Argon_AGET_halfway'
export REST_ISOTOPE=$1
export ELECTRONICS_COMPONENT='Cap'
export ELECTRONICS_POSITION='BottomCentre'
export REST_NEVENTS=$2
echo $REST_ISOTOPE
restG4 $HOME/RPE_IAXO_REST_v2.2.10/IAXO_AGET-REST/G4sims/restSims/AGET/Electronics_halfway/IsotopeSAFEC_halfway.rml