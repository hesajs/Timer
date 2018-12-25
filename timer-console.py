import time
import os 

os.system("clear")
minutes = int(input("Enter the minutes: "))
sec = minutes*60
min = minutes
elapsed_min=0
for i in range(1, minutes*60+1):
    time.sleep(1)
    sec-=1
    os.system("clear")
    
    if(i%60==0):
        elapsed_min+=1
        min-=1
    print(f"Number of miutes: {minutes}\n")
    print("--------------------------------------------")
    print(f"\t|    Time Elapsed: {elapsed_min}: {i%60}    |")
    print("--------------------------------------------\n\n\n")

    print("--------------------------------------------")
    print(f"\t|    Time Remaining: {min}: {sec%60}    |")
    print("--------------------------------------------")

