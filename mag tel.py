#importing stuff
import telnetlib
import getpass
import csv

#variables
x = 1



#converting to byte data
FirstGoal ="0 Magrathea NTS GW (ntsapi.c(V0.1))"
FirstGoal_Byte = FirstGoal.encode()

#getting connection details
HOST = "api.magrathea-telecom.co.uk"
user = input("Enter your remote account: ")
password = input("insert password: ")

#constructing the login
login = "AUTH " + user + " " + password
login_byte = login.encode()


#connecting
tn = telnetlib.Telnet(HOST,777)



#logging in
tn.read_until(FirstGoal_Byte)


tn.write(login_byte + b"\n")





# choosing what is to be done with the number

destination = input("please choose the server you want to point the numbers at: 1 for s1, 2 for s2")

while x == x<1082:
#opening the csv
    with open('insertcsv.csv', 'r') as f:
        str_list = [row[0] for row in csv.reader(f)]     # pulls the first row from csv
        y = ('0' + str_list[x]) #appends a 0
        z = ('44' + str_list[x]) # appends a 44
        if destination == str(1):
                print (y)#this is just for peace of mind could probably be removed
                print (z) 
                command = ('SET ' + y + ' 1 S:'+ z + '@server1') #builds the command that will be set
                print (command)#this is just for peace of mind could probably be removed
                command_byte = command.encode()#encodes the command so it can be read by the api
                tn.write(command_byte)#sends the command by telnet
                x=x+1
        elif destination == str(2):
                print (y)
                print (z)
                command = ('SET ' + y + ' 1 S:'+ z + '@server2')
                print (command)
                command_byte = command.encode()
                tn.write(command_byte)
                x=x+1
    


tn.write(b"QUIT" + b"\n")
print (tn.read_all()) #allows the user to check for mistakes
