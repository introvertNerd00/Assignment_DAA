# ------------------- libraries to be used ---------------------------

import time
import pandas as pd
import matplotlib.pyplot as plt
from is_non_decreasing import insertionSort_nonDec

#---------------  Insertion Sort function (Non-Increasing) --------------------------------
def insertionSort_nonInc(fdata):
    for i in range(1, len(fdata)):
        key = fdata[i]
        j = i - 1
        while j >= 0 and key > fdata[j]:
            fdata[j + 1] = fdata[j]
            j -= 1
        fdata[j + 1] = key
    return fdata


# ---------------------- Read the modified dataset ---------------------------------------
input_data = pd.read_csv("clean_data.csv")


# ----------------- storing processing time -------------------------------------
proc_time={}

# ---------------------- Columns to be used for processing -------------------------------
required_columns = [
    'Current Loan Amount', 'Credit Score', 'Annual Income', 'Monthly Debt',
    'Years of Credit History', 'Months since last delinquent', 'Number of Open Accounts',
    'Number of Credit Problems', 'Current Credit Balance', 'Maximum Open Credit',
    'Bankruptcies', 'Tax Liens'
]

#---------------------------------- Loop for execution  --------------------------
for column in required_columns:
    data = input_data[column].tolist()

#---------------------------------- Calculate the time for sorting ---------------------
    starting_time = time.time()
    sorted_data = insertionSort_nonInc(data)
    processing_time = time.time() - starting_time


#----------------Saving processing times in dictionary-------------------------
    proc_time[column]=processing_time
#----------------- Printing processing times ----------------------------------
    print("Execution time for non-increasing insertion sort of ",column,":", {processing_time} ,"seconds")

#--------------- Saving sorted data -------------------------------------------a
    input_data[column] = sorted_data

#----------------- Saving sorted data to file ---------------------------------
input_data.to_csv("Insert_nonInc.csv", index=False)


#------Plotting execution time graphs ------------------------------------------

categories = list(proc_time.keys())
times= list(proc_time.values())

plt.bar(categories,times)
plt.xlabel('Categories')
plt.ylabel('Time')
plt.title('Execution of Merge sort Non-increasing Order')

plt.show()
