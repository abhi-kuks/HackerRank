Question : 

#take rows and columns and convert both of them to integer using map function 
rows,columns = map(int,input().split())
#Middle row where "WELCOME" will be written
middle = rows//2+1
#Top part of door mat
for i in range(1,middle):
    #calculate number of .|. required and multiply with .|.
    center = (i*2-1)*".|."
    #Moving our center pattern to center using string.center method and filling left and part with "-" 
    print(center.center(columns,"-"))
#print middle part welcome
print("WELCOME".center(columns,"-"))
#create bottom part in reverse order like we did in the top part
for i in reversed(range(1,middle)):
    center = (i*2-1)*".|."
    print(center.center(columns,"-"))
