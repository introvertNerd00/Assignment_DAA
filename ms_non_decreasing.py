# ------------------- libraries to be used ---------------------------

import time
import pandas as pd
import matplotlib.pyplot as plt


#---------------------defining function: Merge Sort (non-decreasing)------------

def  non_dec_m_sort(fdata):
    if len(fdata) <= 1:
        return fdata

    mid = len(fdata) // 2
    left_half = fdata[:mid]
    right_half = fdata[mid:]

    left_half = non_dec_m_sort(left_half)
    right_half = non_dec_m_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
#-------------------------------------------------------------------


proc_time={}
# ---------------------- Read the modified dataset ---------------------------------------
input_data = pd.read_csv("clean_data.csv")


required_columns = [
    'Current Loan Amount', 'Credit Score', 'Annual Income', 'Monthly Debt',
    'Years of Credit History', 'Months since last delinquent', 'Number of Open Accounts',
    'Number of Credit Problems', 'Current Credit Balance', 'Maximum Open Credit',
    'Bankruptcies', 'Tax Liens'
]

#----------------loop to sort each column-------------------------------------
for column in required_columns:
    data = input_data[column].tolist()

#----------------- Calculate the time for sorting -------------
    starting_time = time.time()
    sorted_data = non_dec_m_sort(data)
    processing_time = time.time() - starting_time

#----------------Saving processing times in dictionary-------------------------
    proc_time[column]=processing_time

#--------------- Saving sorted data -------------------------------------------
    input_data[column] = sorted_data

    print(f"Execution time for non-decreasing merge sort of {column}: {processing_time} seconds")
   


#----------------- Saving sorted data to file ---------------------------------
input_data.to_csv("merge_nonDec.csv", index=False)


#------Plotting execution time graphs ------------------------------------------

categories = list(proc_time.keys())
times= list(proc_time.values())

plt.bar(categories,times)
plt.xlabel('Categories')
plt.ylabel('Time')
plt.title('Execution of Merge sort Non-decreasing Order')

plt.show()



