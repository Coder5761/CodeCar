import os
import datetime
import collections
import functools
import inspect
import textwrap
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json
import streamlit as st

# print("Start of the program")


def cache_on_button_press(label, **cache_kwargs):
    internal_cache_kwargs = dict(cache_kwargs)
    internal_cache_kwargs['allow_output_mutation'] = True
    internal_cache_kwargs['show_spinner'] = False
    def function_decorator(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            @st.cache(**internal_cache_kwargs)
            def get_cache_entry(func, args, kwargs):
                class ButtonCacheEntry:
                    def __init__(self):
                        self.evaluated = False
                        self.return_value = None
                    def evaluate(self):
                        self.evaluated = True
                        self.return_value = func(*args, **kwargs)
                return ButtonCacheEntry()
            cache_entry = get_cache_entry(func, args, kwargs)
            if not cache_entry.evaluated:
                if st.button(label):
                    cache_entry.evaluate()
                else:
                    raise st.ScriptRunner.StopException
            return cache_entry.return_value
        return wrapped_func
    return function_decorator
def submit(name):
        # print("hello")
        @cache_on_button_press('submit')
        def check():
            name == "Test"
        if(check()):
            # print(array[spot-1][0], spot)
            spotValue = st.write("This is a free spot")
            array[spot-1][0] = 1
            array[spot-1][1]= name_spot
            array[spot-1][2]= car
            array[spot-1][3]= car_color
            sizes[spot-1]= sizes[spot-1]+1
            money_given = randint(5, 10) * 1
            money = money + money_given
            # print(array)
            # print(str(name_spot)+" paid $"+str(money_given)+" to you")
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
def display_func_source(func):
    code = inspect.getsource(confirm_button_example)
    code = '\n'.join(code.splitlines()[1:]) # remove first line
    st.code(textwrap.dedent(code))

    # input1=int(input("What is the size of parking lots?: "))
input1 = int(st.text_input("What is the size of the parking lots",('10')))
on = True
SavNum = 0
# if(on == False and st.button("Do if you want to reset")):   
array=[[0 for i in range(4)] for j in range(int(input1))]
strArray = ""
money = 0
spots1 = []
value1=0
jsonCount = 0
jsonCount1 = 0
sizes = [0 for i in range(input1)]
labels = [0 for i in range(input1)]
sizes1 = [0 for i in range(input1)]   
# print(labels)
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
                # print(number[0])
                jsonCount = int(number[0])
            for number in p[str(jsonCount)]:
                # print('Date: '+ number['Date'])
                # print('Time: '+ number['Time'])
                # print('Reason: '+ number['Reason'])
                # print('Name: '+ number['Name'])
                # print('Paid: '+ number['Paid'])
                # print('Car Name: '+ number['CarName'])
                # print('Car Color: '+ number['CarColor'])
                # print('Total Revenue: '+ number['TotalRevenue'])
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

def write_json1(data, filename='Array.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=5) 

def log_load1():
    global jsonCount1
    global money
    global array
    global SavNum
    global strArray
    with open("Array.json") as f:
        data = json.load(f)
        for p in data['Data']:   
            for number in p.items():
                jsonCount1 = int(number[0])
            for number in p[str(jsonCount1)]:
                print(number)
                SavNum = number['Spots']
                strArray = number['Array']

log_load()
log_load1()
ask_when = st.selectbox('What would you like to do(choose commands if you are confused):',('','reserve', 'free','graph','save','load','leave','balance','commands'), key = 'Main')
# while on:
    # ask_when=input("What would you like to do(type commands if you are confused): ")
if(ask_when == "reserve"):
        # spot = int(input("which spot would you like to take?: "))
        # name_spot = str(input("Please tell us your name?: "))
        # car = str(input("Please tell us your car type and brand?: "))
        # car_color = str(input("Please tell us your car's color?: "))
    # print(labels)
    spot = int(st.text_input("which spot would you like to take?: ",('0')))
    name_spot = st.text_input("Please tell us your name?: ")
    car = st.text_input("Please tell us your car type and brand?: ")
    car_color = st.text_input("Please tell us your car's color?: ")
    # @cache_on_button_press('submit')
    # if(array[spot-1][0] == 1):
    #     spotValue = st.write("Sorry, Spot Token")
    #     # print(array[spot-1][0], "no work")
    # else:
    if(st.button('Submit')):
        # print(array[spot-1][0], spot)
        spotValue = st.write("This is a free spot")
        print(SavNum)
        print(input1)
        if(int(SavNum) != input1):
            SavNum = input1
            print(input1 != SavNum)
            array=[[0 for i in range(4)] for j in range(int(input1))]
        print(array)
        array[spot-1][0] = 1
        array[spot-1][1]= name_spot
        array[spot-1][2]= car
        array[spot-1][3]= car_color
        sizes[spot-1]= sizes[spot-1]+1
        money_given = randint(5, 10) * 1
        money = money + money_given
        print(array) 
        # print(str(name_spot)+" paid $"+str(money_given)+" to you")
        with open("Array.json") as file:
            strArray = str(array)
            data1 = {}
            print('geen test')
            jsonCount1+=1
            data1[str(jsonCount1)] = []
            data1[str(jsonCount1)].append({
                'Spots': str(SavNum),
                'Array': array
            })
            data = json.load(file)
            temp = data['Data']
            temp.append(data1)
        write_json1(data)
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
elif(ask_when == "save"):
    save(array,money,turns,multiplier,sizes1,sizes)
elif(ask_when == "load"):
    load()
elif(ask_when == "leave"):
    input3 = st.selectbox("Are you sure, all unsaved changes will be discared: ",('','yes','no'))
    if(input3 == "yes"):
        st.write("Ok, have a nice day")
        st.write("Also you now have $"+ str(money)+" after a long day of work")
        os.exit(0)
    else:
        st.write("I see, it's good to save")
elif(ask_when == "balance"):
    st.write("Balance: $" + str(money))
elif(ask_when == "commands"):
    st.write("Reserve: Asks which free do you want to be taken and take the spot and name of customer")
    st.write("Free: ask the customer name to free the spot")
    st.write("Save: will save all your progress, can be saved to multiple files")
    st.write("Load: will load progress based on the file number")
    st.write("Leave: will stop the simulation !WARNING! all unsaved progress will be discarded when you leave")
    st.write("Balance: shows how much money you have now")
    st.write("Graph: shows how much a spot has been reserved or taken")
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

