#S19 File Analysis

##functions##

#Count SX records in the file
def s_count(record_list, record_num):
    c=0
    r=record_list
    l=len(r) #length of the list
    s= "S"+str(record_num) #S0, S1, S2, S3, S4,..
    for i in range(0, l-1):
        t= s in r[i]
        if t==True:
            c+=1
    return c

#List the SX counts, where X is 0 through 9
def s_totals(record_list):
    r=record_list
    S=zerolist(10)
    for i in range(0,9):
        S[i]=s_count(r,i)
    return S

#Print Totals
def print_totals(S):
    for i in range(0,9):
        if S[i]!=0:
            print(str(S[i])+'\tS'+str(i)+' records.')
    return

def zerolist(n):
    l=[0]*n
    return l

#extracts the bytecount byte from record
def bytecount_byte(s):
    r=s[2:4]
    return r
#converts bytecount from hex to decimal value
def bytecount(s):
    b=bytecount_byte(s)
    r=int(b,16)
    return r

#extracts the checksum from a record
def checksum(s):
    r=s[-2:]
    return r

#extracts the data from a record
def data_extract(r):
    adc=r[4:] #address, data, checksum
    if 'S0' in r or 'S1' in r:
        s=r[8:-2]
    if 'S2' in r:
        s=r[10:-2]
    if 'S3' in r or 'S7' in r:
        s=r[12:-2]
    return s

def addr_extract(r):
    adc=r[4:] #address, data, checksum
    if 'S0' in r or 'S1' in r:
        s=r[4:8]
    if 'S2' in r:
        s=r[4:10]
    if 'S3' in r or 'S7' in r:
        s=r[4:12]
    return s

#extracts address data of an entire list of records
def addr_extract_whole(record_list):
    r=record_list
    l=len(record_list)
    S=zerolist(l)
    for i in range(0,l-1):
        S[i]=addr_extract(r[i])
    return S

def data_extract_whole(record_list):
    r=record_list
    l=len(record_list)
    S=zerolist(l)
    for i in range(0,l-1):
        S[i]=data_extract(r[i])
    return S
def dump_data(g):
    q=data_extract_whole(g)
    data=open('_data.txt','w')
    for x in q:
        data.write("%s\n" % x)
    return
def dump_addresses(g):
    q=addr_extract_whole(g)
    data=open(file_name+'_addresses.txt','w')
    for x in q:
        data.write("%s\n" % x)
    return

####MAIN PROGRAM####
#Prompt user for file name. Save file name to var
file_name= raw_input('Enter file name: ')
#Read file to memory
f=open(file_name,'r')
#Store file data to var
f_data=f.read()
#breakdown S19 records into list
g='\r\n'
if g in f_data:
    h=f_data.split(g)
else:
    h=f_data.split('\n')

#Print total number of records
print file_name + ' has ' + str(len(h)) + ' records.'

#Make list of the count of different type of S records
z=s_totals(h)
print_totals(z)
d_h=data_extract_whole(h)
a_h=addr_extract_whole(h)


