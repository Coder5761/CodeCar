     for i in range(input1):
            if(array[i][1] == spot):
                array[i][0]=0
                name_spot = array[i][1]
                car = array[i][2]
                car_color = array[i][3]
                array[i][1]="clear"
                array[i][2]="clear"
                array[i][3]="clear"
                found=True
                spots = array[i][0]
                sizes1[spots-1]= sizes[spots-1]+1
                money_given = randint(15,20)
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
