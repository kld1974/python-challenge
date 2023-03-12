#PyBank
import os
import csv

def f_cur(myval):
    return '${:,.2f}'.format(myval)
#IMPORT & OUTPUT FILES
orig_csv = os.path.join('python-challenge/PyBank/Resources', 'budget_data.csv')
output = "python-challenge/PyBank/Analysis/answers.txt"
#VARIABLES
fr = 0
mon = 0
total = 0
rev_p = 0
mon_chg = []
rev_c = 0
GD = ["", 9999999]
GI = ["", 0]
chg_list = []
avg = 0

#OPEN FILE
with open(orig_csv) as csvfile:  
    csvreader = csv.DictReader(csvfile)
    csv_header = next(csvreader)
    #LOOP THRU ROWS
    for row in csvreader:
        mon += 1
        #TOTAL
        total = total + int(row["Profit/Losses"])
        #AVG
        if fr == 0:
            fr = float(row["Profit/Losses"])
       
        rev_c = float(row["Profit/Losses"])- rev_p
        rev_p = float(row["Profit/Losses"])
        
        chg_list = chg_list + [rev_c]
        mon_chg = [mon_chg] + [row["Date"]]

        #GREAT INCREASE
        if rev_c > GI[1]:
            GI[0] = row['Date']
            GI[1] = rev_c     
        #GREAT DECREASE 
        if rev_c < GD[1]:
            GD[0] = row['Date']
            GD[1]= rev_c
    avg = ((sum(chg_list)-fr)/(len(chg_list)-1))

#PRINT RESULTS
print("---Financial Analysis---")
print("Total Months: " + str(mon))
print("Total : " + str(f_cur(total)))
print("Avg Chg: " + str(f_cur(avg)))
print("Greatest Increase: " + GI[0] + " " + str(f_cur(GI[1])))
print("Greatest Decrease: " + GD[0] + " " + str(f_cur(GD[1])))

#WRITE TO FILE
with open(output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write("Total Months: %d\n" % mon)
    file.write("Total Revenue: %s\n" % f_cur(total))
    file.write("Average Revenue Change %s\n" % f_cur(avg))
    file.write("Greatest Increase in Profits: %s %s\n" % (GI[0], f_cur(GI[1])))
    file.write("Greatest Decrease in Profits: %s %s\n" % (GD[0], f_cur(GD[1])))


    