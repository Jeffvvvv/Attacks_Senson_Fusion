
fin = open("sample-laser-radar-measurement-data-1", "r")
fout = open("L_10_1.txt", "w")
# header line
header = fin.readlines()
#fout.write(header)
# data lines
row = 100
angle = 0
for line in range(row):
    dat_in = header[line].split()
    if dat_in[0] == "L":
    	#dat_in[1] = str(float(dat_in[1]) + 1) # modify data
    	dat_in[1] = dat_in[1]*math.sin(angle)
    	dat_in[2] = dat_in[2]*math.cos(angle)

    if dat_in[0] == 'R':
        angle = dat_in[2]

    dat_out = " ".join(dat_in)
    fout.write(dat_out+"\n")

for line in range(row,len(header)):
	fout.write(header[line])

fin.close()
fout.close()
