import sys


NEVENTS=str(sys.argv[1])
ISOTOPE=str(sys.argv[2])
COMPONENT=str(sys.argv[3])

if sys.argv[4] == "None":
	POSITION=""
else:
	POSITION=str(sys.argv[4])

RUNNUMBER=str(sys.argv[5])

outfile = open(ISOTOPE+'From'+COMPONENT+POSITION+'_halfway_'+RUNNUMBER+'temp.rml','w')

outfile.write('<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\" ?>\n\n')

outfile.write('<restG4>\n\n')

outfile.write('<globals>\n')
outfile.write('    <variable name=\"REST_DATAPATH\" value=\"${HOME}/RPE_IAXO_REST_v2.2.10/data\" overwrite=\"true\" />\n')
outfile.write('    <variable name=\"EXPERIMENT\" value=\"IAXOD0\" overwrite=\"false\" />\n')
outfile.write('    <variable name=\"VERSION\" value=\"2.29\" overwrite=\"false\" />\n')
outfile.write('    <variable name=\"IAXOD0_PATH\" value=\"${HOME}/RPE_IAXO_REST_v2.2.10/IAXO_AGET-REST\" overwrite=\"true\" />\n')
outfile.write('    <variable name=\"IAXOD0_DATAPATH\" value=\"${REST_DATAPATH}/IAXOD0\" overwrite=\"true\" />\n')
outfile.write('    <variable name=\"IAXOD0_G4PATH\" value=\"${IAXOD0_PATH}/G4sims\" overwrite=\"true\" />\n')
outfile.write('    <variable name=\"IAXOD0_GEOPATH\" value=\"${IAXOD0_G4PATH}/geometry\" overwrite=\"true\" />\n')
outfile.write('    <variable name=\"IAXOD0_GEODIR\" value=\"Argon_AGET_halfway\" overwrite=\"true\" />\n')
outfile.write('    <variable name=\"REST_NEVENTS\" value=\"'+NEVENTS+'\" overwrite=\"true\" />\n')
outfile.write('    <variable name=\"REST_ISOTOPE\" value=\"'+ISOTOPE+'\" overwrite=\"true\" /> \n')
outfile.write('    <variable name=\"ELECTRONICS_COMPONENT\" value=\"'+COMPONENT+'\" overwrite=\"true\" /> \n')
outfile.write('    <variable name=\"ELECTRONICS_POSITION\" value=\"'+POSITION+'\" overwrite=\"true\" />\n')
outfile.write('    <variable name=\"REST_VOLUME\" value=\"${ELECTRONICS_COMPONENT}${ELECTRONICS_POSITION}PhysVolume\" overwrite=\"true\" />\n')
outfile.write('    <variable name=\"DIR_DATA\" value=\"${REST_ISOTOPE}_${ELECTRONICS_COMPONENT}${ELECTRONICS_POSITION}\" overwrite=\"true\" /> \n')
outfile.write('    <parameter name=\"mainDataPath\" value=\"${IAXOD0_DATAPATH}/${IAXOD0_GEODIR}/${DIR_DATA}\" />\n')
outfile.write('    <parameter name=\"gasDataPath\" value=\"${REST_PATH}/data/gasFiles\" />\n')
outfile.write('    <parameter name=\"verboseLevel\" value=\"warning\" /> \n')
outfile.write('    <variable name=\"RUN_NUMBER\" value=\"'+RUNNUMBER+'\" overwrite=\"true\" /> \n')
outfile.write('</globals>\n')



with open('simfile_endpart.txt','r') as rest_of_file:
	for line in rest_of_file:
		outfile.write(line)