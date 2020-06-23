# import the csv file
import os
import csv
filepath = os.path.join("learnpython", "budget_data.csv")

# open the csv
with open("budget_data.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csv_reader)

    # set variables, arrays
    Months = 0
    Net_Revenue = 0
    Average_Revenue_Change = 0
    Total_Change = 0
    Max_Increase_Change = 0
    Max_Decrease_Change = 0

    Date = []
    Revenue = []
    Revenue_Change = []

    Max_Increase_Date = None
    Max_Decrease_Date = None

    # create loop to find number of Months
    for row in csv_reader:
        Months += 1

        # find Net_Revenue
        Net_Revenue = Net_Revenue + int(row[1])

        # append each column
        Date.append(row[0])
        Revenue.append(row[1])

    # find average of the changes for the entire period
    for i in range(len(Revenue)-1):
        Total_Change = int(Revenue[i]) - int(Revenue[i-1])
        Revenue_Change.append(Total_Change)
    Average_Revenue_Change = (Total_Change/Months)

    # find the largest changes month to month
    Max_Increase_Change = max(Revenue_Change)
    Max_Decrease_Change = min(Revenue_Change)

    # put the dates with the maxs
    Max_Increase_Date = str(Date[Revenue_Change.index(max(Revenue_Change))])
    Max_Decrease_Date = str(Date[Revenue_Change.index(min(Revenue_Change))])

    # print the outputs
    print("Financial Analysis")
    print("Total Months: " + str(Months))
    print("Total Revenue: " + " $" + str(Net_Revenue))
    print("Average Change: " + " $" + str(round(Average_Revenue_Change)))
    print("Largest Monthly Increase: " + str(Max_Increase_Date) + " $" + str(Max_Increase_Change))
    print("Largest Monthly Decrease: " + str(Max_Decrease_Date) + " $" + str(Max_Decrease_Change))

    # create the txt file for the output
    text_path = "pybank_results.txt"
    with open(text_path, "w") as txt_file:
        txt_file.write("Total Months: " + str(Months) + "\r\n" 
        
        "Total Revenue: " + " $" + str(Net_Revenue) + "\r\n" 

        "Average Change: " + " $" + str(round(Average_Revenue_Change)) + "\r\n" 

        "Largest Monthly Increase: " + str(Max_Increase_Date) + " $" + str(Max_Increase_Change) + "\r\n" 

        "Largest Monthly Decrease: " + str(Max_Decrease_Date) + " $" + str(Max_Decrease_Change))


