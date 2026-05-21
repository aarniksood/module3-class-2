#write a program to define shutdown function
def shutdown():
    print("shutting down... please wait")
    exit()

a = input("do you want to shutdown. (yes/no)")
    
if a == 'yes':
    shutdown()
else:
    print("there is no other function so wait for battery to run out cause you denied the shutdown")
print("1 + 1 = 11")