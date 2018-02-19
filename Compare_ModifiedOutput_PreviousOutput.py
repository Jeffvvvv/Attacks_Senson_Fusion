fin = open("output.txt", "r")
fin2 = open("output_3_LR_10 2.txt","r")
header = fin.readlines() 
count = 0
header2 = fin2.readlines()
for line in range(len(header)):
    dat_in = header[line].split()
    dat_in2 = header2[line].split()
    if abs(float(dat_in[0])-float(dat_in2[0]))>0.01:
    	count = count+1
print count
    #print(line,float(dat_in[1])-float(dat_in2[1]))

gcloud compute scp gpu-deep-learner:~/class ~/Downloads/class --zone us-central1-a
