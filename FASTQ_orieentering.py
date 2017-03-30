import sys
import gzip

line = 0
orientation=1


read_pair=[]
for line in gzip.open(sys.argv[1]):
	read_pair.append( line.strip() )
	if len(read_pair) == 8:
		if read_pair[0] == read_pair[4]:
			read_pair[0] += " 1:N:0:NNNNNN"
			read_pair[4] += " 2:N:0:NNNNNN"
		else:
			print "ERROR: unpaired read/disordered fastq"
			quit()

		for read in read_pair:
			print read
		read_pair = []
