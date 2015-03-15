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
