import os
import csv

input_path=os.path.join('Resources','budget_data.csv')


with open(input_path,"r",encoding='utf-8')as csv_file:
    csvreader=csv.reader(csv_file,delimiter=",")
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

    #average change,max and min       
    difference_list=[]    
    for i in range(0,Total_Month-1):
        change=datalist[-1]-datalist[0]
        average_change=round(change/(Total_Month-1),2)

        difference=datalist[i+1]-datalist[i]
        difference_list.append(difference)    

    maxnum=max(difference_list)
    minnum=min(difference_list)
    
    P_max=difference_list.index(maxnum)
    P_min=difference_list.index(minnum)

    date1=timelist[P_max+1]
    date2=timelist[P_min+1]
    
    print('Financial Analysis')
    print('-'*30)
    print(f'Total Month:{str(Total_Month)}')
    print(f'Total:{str(Total)}')
    print(f'Average Change:{str(average_change)}')
    print(f'Greatest Increase in Profits:({str(date1)}) (${str(maxnum)})')
    print(f'Greatest Decrease in Profits:({str(date2)}) (${str(minnum)})')   


output_path=os.path.join('analysis','summary.csv')

with open(output_path,'w',encoding='utf-8')as csv_file:
    csvwriter=csv.writer(csv_file,delimiter=",")
    
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["-"*30])
    csvwriter.writerow([f'Total Month:{str(Total_Month)}'])
    csvwriter.writerow([f'Total:{str(Total)}'])
    csvwriter.writerow([f'Average Change:{str(average_change)}'])
    csvwriter.writerow([f'Greatest Increase in Profits:({str(date1)}) (${str(maxnum)})'])
    csvwriter.writerow([f'Greatest Decrease in Profits:({str(date2)}) (${str(minnum)})'])