import os
import datetime
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json
import streamlit as st


    # input1=int(input("What is the size of parking lots?: "))
input1 = int(st.text_input("What is the size of the parking lots"))
    
array=[[0 for i in range(4)] for j in range(int(input1))]
money = 0
on = False
spots1 = []
value1=0
found = False
turns = 0
jsonCount = 0
multiplier = 1
labels = [0 for i in range(input1)]
sizes = [0 for i in range(input1)]
sizes1 = [0 for i in range(input1)]

for r in range(input1):
    labels[r] = str(r+1)
    
for i in range(input1):
    array[i][1]="clear"
    array[i][2]="clear"
    array[i][3]="none"

def save(array,money,turns,multiplier,free,reserve):
    global input1
    input2 = input("What Save?(type in a save number): ")
    write = "save"+input2+".txt"
    with open(write,"w") as file:
        for i in range(int(input1)):
            file.write(str(array[i][0])+" ")
            file.write(str(array[i][1])+" ")
            file.write(str(array[i][2])+" ")
            file.write(str(array[i][3])+"\n")
        file.write(str(money)+"\n")
        file.write(str(turns)+"\n")
        file.write(str(multiplier)+"\n")
        for i in range(int(input1)):
            file.write(str(reserve[i])+"\n")
        for i in range(int(input1)):
            file.write(str(free[i])+"\n")
        file.write(str(input1)+"\n")
        
def load():
    global array
    global money
    global turns
    global multiplier
    global sizes1
    global sizes
    global input1
    global labels
    number = 0
    input2 = input("What Save?(type in a save number): ")
    write = "save"+input2+".txt"
    with open(write,"r") as file:
        for i in file:
            pass
        input1 = int(i)
    array=[[0 for i in range(4)] for j in range(int(input1))]
    sizes1=[0 for i in range(int(input1))]
    sizes=[0 for i in range(int(input1))]
    labels=[0 for i in range(int(input1))]
    number = 0
    number1 = 0
    Reserve = None
    with open(write,"r") as file:
        line = file.readlines()
        file = [l.strip() for l in line]
        for i in file:
            if(number == input1):
                Reserve = True
                money = int(i)
                number += 1
                continue
            if(Reserve == None):
                value1,value2,value3,value4=i.split(" ")
                array[number][0] = value1
                array[number][1] = value2
                array[number][2] = value3
                array[number][3] = value4
                number = number + 1
            elif(number == input1 + 1):
                turns = int(i)
                number += 1
                continue
            elif(number == input1 + 2):
                multiplier = int(i)
                number += 1
                continue
            if(number1 == input1):
                Reserve = False
                number1 = 0
                number += number1
            if(Reserve == True):
                sizes[number1] = int(i)
                number1 +=1
            elif(Reserve == False):
                if(number == (input1*4) + 3):
                    return
                sizes1[number1] = int(i)
                number1 +=1
                number += 1

def buy():
    global money
    global turns
    global multiplier
    choice_c = True
    while choice_c:
        choice = input("what would you like to buy? ")
        if(choice == "energy drink"):
            if(money - 30 < 0):
                print("sorry not enough money")
                break 
            else:
                print("choice done")
                turns = 3
                multiplier = 2
                money = money - 30
                break
    return

def log_load():
    global money
    global jsonCount
    with open("log_sheet.json") as f:
        data = json.load(f)
        for p in data['Data']:   
            for number in p.items():
                print(number[0])
                jsonCount = int(number[0])
            for number in p[str(jsonCount)]:
                print('Date: '+ number['Date'])
                print('Time: '+ number['Time'])
                print('Reason: '+ number['Reason'])
                print('Name: '+ number['Name'])
                print('Paid: '+ number['Paid'])
                print('Car Name: '+ number['CarName'])
                print('Car Color: '+ number['CarColor'])
                print('Total Revenue: '+ number['TotalRevenue'])
                value1 = number['Date']
                value2 = number['Time']
                value3 = number['Reason']
                value4 = number['Name']
                value5 = number['Paid']
                value6 = number['CarName']
                value7 = number['CarColor']
                value8 = number['TotalRevenue']

def write_json(data, filename='log_sheet.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=5) 

log_load()

ask_when = st.selectbox('What would you like to do(choose commands if you are confused):',('','reserve', 'free'), key = 'Main')
# while on:
    # ask_when=input("What would you like to do(type commands if you are confused): ")
if(ask_when == "reserve"):
        # spot = int(input("which spot would you like to take?: "))
        # name_spot = str(input("Please tell us your name?: "))
        # car = str(input("Please tell us your car type and brand?: "))
        # car_color = str(input("Please tell us your car's color?: "))
    spot = int(st.text_input("which spot would you like to take?: "))
    name_spot = st.text_input("Please tell us your name?: ")
    car = st.text_input("Please tell us your car type and brand?: ")
    car_color = st.text_input("Please tell us your car's color?: ")
    if(array[spot-1][0] == 1):
        print("sorry, this spot is already reserved, try again")
    else:
        array[spot-1][0]=1
        array[spot-1][1]= name_spot
        array[spot-1][2]= car
        array[spot-1][3]= car_color
        sizes[spot-1]= sizes[spot-1]+1
        money_given = randint(5, 10) * multiplier
        money = money + money_given
        print(str(name_spot)+" paid $"+str(money_given)+" to you")
        with open("log_sheet.json") as file:
            now = datetime.datetime.now()
            nowstr = now.strftime("%H:%M:%S")
            nowstr1 = now.strftime("%m,%d,%Y")
            data1 = {}
            jsonCount+=1
            data1[str(jsonCount)] = []
            data1[str(jsonCount)].append({
                'Date': str(nowstr1),
                'Time': str(nowstr),
                'Reason': 'Reserved',
                'Name': str(name_spot),
                'Paid': str(money_given),
                'CarName': str(car),
                'CarColor': str(car_color),
                'TotalRevenue': str(money)
            })
            data = json.load(file)
            temp = data['Data']
            temp.append(data1)
        write_json(data)
        # file.write("\n")
        # file.write(nowstr)
        # file.write("Reason:_Reserved ")
        # file.write(str(name_spot))
        # file.write("_paid_"+str(money)+" ")
        # file.write("Car:_"+str(car) + " Car_color:_"+str(car_color)+" Total_Revenue: "+str(money))
# elif(ask_when == "free"):
#     try:
#         spot = str(input("Please tell us your name: "))
#     except:
#         print("sorry, I couldn't get you try again")
#         os._exit(0)
#     for i in range(input1):
#         if(array[i][1] == spot):
#             array[i][0]=0
#             name_spot = array[i][1]
#             car = array[i][2]
#             car_color = array[i][3]
#             array[i][1]="clear"
#             array[i][2]="clear"
#             array[i][3]="clear"
#             found=True
#             spots = array[i][0]
#             sizes1[spots-1]= sizes[spots-1]+1
#             money_given = randint(15,20) * multiplier
#             money = money + money_given
#             print(str(name_spot)+" paid $"+str(money_given)+" to you")
#             with open("log_sheet.json") as file:
#                 now = datetime.datetime.now()
#                 nowstr = now.strftime("%H:%M:%S")
#                 nowstr1 = now.strftime("%m,%d,%Y")
#                 data1 = {}
#                 jsonCount+=1
#                 data1[str(jsonCount)] = []
#                 data1[str(jsonCount)].append({
#                     'Date': str(nowstr1),
#                     'Time': str(nowstr),
#                     'Reason': 'Freed',
#                     'Name': str(name_spot),
#                     'Paid': str(money_given),
#                     'CarName': str(car),
#                     'CarColor': str(car_color),
#                     'TotalRevenue': str(money)
#                 })
#                 data = json.load(file)
#                 temp = data['Data']
#                 temp.append(data1)
#         write_json(data)              
#     if(found == False):
#         print("sorry, this spot is a free one, try again")
elif(ask_when == "list"):
    print(array)
elif(ask_when == "buy"):
    buy()
elif(ask_when == "save"):
    save(array,money,turns,multiplier,sizes1,sizes)
elif(ask_when == "load"):
    load()
elif(ask_when == "leave"):
    input3 = input("Are you sure, all unsaved changes will be discared: ")
    if(input3 == "yes"):
        print("Ok, have a nice day")
        print("Also you now have $"+ str(money)+" after a long day of work")
        os.exit(0)
    else:
        print("I see, it's good to save")
elif(ask_when == "balance"):
    print("Balance: $" + str(money))
elif(ask_when == "commands"):
    print()
    print("Reserve: Asks which free do you want to be taken and take the spot and name of customer")
    print("Free: ask the customer name to free the spot")
    print("List: shows all free/taken spots available")
    print("Buy: buy things to help you grow and get more money")
    print("Save: will save all your progress, can be saved to multiple files")
    print("Load: will load progress based on the file number")
    print("Leave: will stop the simulation !WARNING! all unsaved progress will be discarded when you leave")
    print("Balance: shows how much money you have now")
    print("Graph: shows how much a spot has been reserved or taken")
    print()
elif(ask_when == "graph"):
    fig1, ax1 = plt.subplots(1,3)
    ax1[0].pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1[0].axis('equal')
    ax1[0].set_title("Reserved spots")
    ax1[1].pie(sizes1, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1[1].axis('equal')
    ax1[1].set_title("Freed Spots")
    # if(spots == []):
    #     spots.append([])
    # else:
    #     spots.append([])
    spots1.append([])
    for i in range(input1):
        spots1[value1].append(int(array[i][0]))

    ax1[2].imshow(spots1)
    # ax1[2].axis('equal')
    ax1[2].set_title("Current Parking lot")
    st.pyplot(fig1)
    value1 += 1
elif(ask_when==""):
    pass
else:
    print("sorry, I couldn't get you try again")
if(turns > 0):
    turns = turns - 1
if(turns == 0):
    multiplier = 1
