#S19 File Analysis
#anovus
#This is a small module which can be used to analyze the structure of
#an S19 file for personal study and reference.

###############
#	Functions
###############

#Returns a count for records of the S[N] type, where N is any number from 0 through 9.

def s_count(record_list, N):
    c=0				#count var initalized at 0
    r=record_list 	#local var for the list of records
    l=len(r) 		#length of the record list (the S19 file)
    s= "S"+str(N)		#Depending on value of N, a string equal to S0, S1, .., S8, or S9
    for i in range(0, l-1):	#iterates for each member of the list
        t= s in r[i]		#Is S[N] found in the current row? True if yes, False if no.
        if t==True:			
            c+=1 			#increment by 1 for each record of S[N] found
    return c

#Returns a list of 10 elements, where the first element is equal to the number of S0
#records in the S19 file, the 2nd element equal to the number of S1 records, and so on
#until S9.

def s_totals(record_list):
    r=record_list	#local var for the list of records
    S=zerolist(10)	#initialize empty list.
    for i in range(0,9):
        S[i]=s_count(r,i)		#count how many of S[N] type records in the S19 file.
    return S

#A printed breakdown of the type of S records found in the S19 file. Omits S type records
#that are not found in the file.

def print_totals(S):
    for i in range(0,9):
        if S[i]!=0:
            print(str(S[i])+'\tS'+str(i)+' records.')
    return

#Initialize a list of zeroes of length N.

def zerolist(N):
    l=[0]*N
    return l

#Extracts the bytecount byte from the selected record R. See S19_Chart for illustration of
#different byte fields for each record.

def bytecount_byte(R):
    r=R[2:4]
    return r

#Converts the bytecount byte from hex to decimal value.

def bytecount(s):
    b=bytecount_byte(s)
    r=int(b,16)
    return r

#Extracts the checksum byte from the selected record R.

def checksum(R):
    r=R[-2:]
    return r

#Extracts the data fields from the selected record R

def data_extract(R):
    adc=R[4:] 			#address, data, checksum
    if 'S0' in R or 'S1' in R:
        s=R[8:-2]
    if 'S2' in R:
        s=R[10:-2]
    if 'S3' in R or 'S7' in R:
        s=R[12:-2]
    return s

#Extracts the address fields from the selecter record R.

def addr_extract(R):
    adc=R[4:] #address, data, checksum
    if 'S0' in R or 'S1' in R:
        s=R[4:8]
    if 'S2' in R:
        s=R[4:10]
    if 'S3' in R or 'S7' in R:
        s=R[4:12]
    return s

#Extracts the address fields for all records in the records list.
#Returns a list of the address fields.

def addr_extract_whole(record_list):
    r=record_list
    l=len(record_list)
    S=zerolist(l)
    for i in range(0,l-1):
        S[i]=addr_extract(r[i])
    return S

#Extracts the data fields for all records in the records list.
#Returns a list of the data fields.

def data_extract_whole(record_list):
    r=record_list
    l=len(record_list)
    S=zerolist(l)
    for i in range(0,l-1):
        S[i]=data_extract(r[i])
    return S

#Saves the extracted data fields list to file.

def dump_data(g):
    q=data_extract_whole(g)
    data=open(file_name+'_data.txt','w')
    for x in q:
        data.write("%s\n" % x)
    return

#Saves the extracted address fields list to file.

def dump_addresses(g):
    q=addr_extract_whole(g)
    data=open(file_name+'_addresses.txt','w')
    for x in q:
        data.write("%s\n" % x)
    return

#####################
#	Main Program	
#####################

#Prompt user for file name. Save file name to var.
file_name= raw_input('Enter file name: ')
#Read file to memory.
f=open(file_name,'r')
#Store file data to var.
f_data=f.read()
#Breakdown S19 records into list.
g='\r\n'
if g in f_data:
    h=f_data.split(g)
else:
    h=f_data.split('\n')

#Print total number of records.
print file_name + ' has ' + str(len(h)) + ' records.'

#Make list of the count of different type of S records.
z=s_totals(h)
print_totals(z)
#Save Data fields to file.
d_h=data_extract_whole(h)
#Save Address fields to file.
a_h=addr_extract_whole(h)
