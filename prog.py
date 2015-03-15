#S19 File Analysis

#Prompt user for file name. Save file name to var
file_name= raw_input('Enter file name: ')
#Read file to memory
f=open(file_name,'r')
#Store file data to var
f_data=f.read()
#breakdown S19 records into list
h=f_data.split('\r\n')

#Print total number of records
print file_name + ' has ' + str(len(h)) + ' records.'
