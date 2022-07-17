import os
import csv

input_path=os.path.join("Resources","election_data.csv")

with open(input_path,"r")as csv_file:
    csvreader=csv.reader(input_path,delimiter",")
