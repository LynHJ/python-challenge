import os
import csv

input_path=os.path.join("Resources","election_data.csv")

with open(input_path,"r",encoding='utf-8')as csv_file:
    csvreader=csv.reader(csv_file,delimiter=",")
    header=next(csvreader)

    Charles_Casper_Stockham=[]
    Diana_DeGette=[]
    Raymon_Anthony_Doane=[]

    for row in csvreader:
        if str('Charles Casper Stockham')==row[2]:
            Charles_Casper_Stockham.append(row[2])     
        if str('Diana DeGette')==row[2]:
            Diana_DeGette.append(row[2])    
        if str('Raymon Anthony Doane')==row[2]:
            Raymon_Anthony_Doane.append(row[2])
    
    #votes for each candidates
    vote1=len(Charles_Casper_Stockham)
    vote2=len(Diana_DeGette)
    vote3=len(Raymon_Anthony_Doane)
    
    Total_votes=int(vote1)+int(vote2)+int(vote3)
    
    rate1=round((int(vote1)/Total_votes)*100,3)
    rate2=round((int(vote2)/Total_votes)*100,3)
    rate3=round((int(vote3)/Total_votes)*100,3)

    votelist=[vote1,vote2,vote3]
    candilist=[str('Charles Casper Stockham'),str('Diana DeGette'),str('Raymon Anthony Doane')]    
   
    maxvote=max(votelist)
    P_maxvote=votelist.index(maxvote)
    winner=candilist[P_maxvote]
    
    print(f'Election Results')
    print('-'*42)
    print(f'Total Votes:{str(Total_votes)}')
    print('-'*42)
    print(f'Charles Casper Stockham:{str(rate1)}% ({str(vote1)})')
    print(f'Diana DeGette:{str(rate2)}% ({str(vote2)})')
    print(f'Raymon Anthony Doane:{str(rate3)}% ({str(vote3)})')
    print('-'*42)
    print(f'Winner:{str(winner)}')
    print('-'*42)


output_path=os.path.join('analysis','votes.txt')

with open(output_path,"w",encoding='utf-8')as txt_file:
    csvwriter=csv.writer(txt_file,delimiter=",")
    
    csvwriter.writerow([f'Election Results'])
    csvwriter.writerow(['-'*42])
    csvwriter.writerow([f'Total Votes:{str(Total_votes)}'])
    csvwriter.writerow(['-'*42])
    csvwriter.writerow([f'Charles Casper Stockham:{str(rate1)}% ({str(vote1)})'])
    csvwriter.writerow([f'Diana DeGette:{str(rate2)}% ({str(vote2)})'])
    csvwriter.writerow([f'Raymon Anthony Doane:{str(rate3)}% ({str(vote3)})'])
    csvwriter.writerow(['-'*42])
    csvwriter.writerow([f'Winner:{str(winner)}'])
    csvwriter.writerow(['-'*42])