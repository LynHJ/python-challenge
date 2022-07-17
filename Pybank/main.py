import os
import csv

input_path=os.path.join('Resources','budget_data.csv')


with open(input_path,"r",encoding='utf-8')as csv_file:
    csvreader=(csv.reader(csv_file,delimiter=","))
    header=next(csvreader)

    #creat list
    datalist=[]
    timelist=[]
    for row in csvreader:
        datalist.append(int(row[1]))
        timelist.append(str(row[0]))

    #total month    
        Total_Month=len(datalist)
        
    #total
    Total=0
    for data in datalist:
        Total+=data

    #average change       
        #[(a2-a1)+(a3-a2)+(a4-a3)]/3=(a4-a1)/3
        change=datalist[-1]-datalist[0]
        length=len(datalist)-1
        average_change=round(change/length,2)

    
    #Max and min
    maxnum=max(datalist)
    minnum=min(datalist)
    
    P_max=datalist.index(maxnum)
    P_min=datalist.index(minnum)

    date1=timelist[P_max]
    date2=timelist[P_min]
    
    print('Financial Analysis')
    print('-'*30)
    print(f'Total month:{str(Total_Month)}')
    print(f'Total:{str(Total)}')
    print(f'Average change:{str(average_change)}')
    print(f'Greatest Increase in Profits:{(str(date1))} {str(maxnum)})')
    print(f'Greatest Decrease in Profits:{str((date2))} {(str(minnum))}')    


output_path=os.path.join('analysis','summary.csv')

with open(output_path,"w",encoding='utf-8')as csv_file:
    csvwriter=csv.writer(csv_file,delimiter=",")
    
    csvwriter.writerow('Financial Analysis')
    csvwriter.writerow('-'*30)
    csvwriter.writerow(f'Total month:{str(Total_Month)}')
    csvwriter.writerow(f'Total:{str(Total)}')
    csvwriter.writerow(f'Average change:{str(average_change)}')
    csvwriter.writerow(f'Greatest Increase in Profits:{(str(date1))} {str(maxnum)})')
    csvwriter.writerow(f'Greatest Decrease in Profits:{str((date2))} {(str(minnum))}')