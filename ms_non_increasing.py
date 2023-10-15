# ------------------- libraries to be used ---------------------------
import time
import pandas as pd
import matplotlib.pyplot as plt

#---------------  Merge Sort function (Non-Increasing) --------------------------------
def non_inc_m_sort(fdata):
    if len(fdata) <= 1:
        return fdata

    mid = len(fdata) // 2
    left_half = fdata[:mid]
    right_half = fdata[mid:]

    left_half = non_inc_m_sort(left_half)
    right_half = non_inc_m_sort(right_half)

    return merge(left_half, right_half)

#---------------  Merge function --------------------------------
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:  
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

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
    sorted_data =non_inc_m_sort(data)
    processing_time = time.time() - starting_time

#----------------Saving processing times in dictionary-------------------------
    proc_time[column]=processing_time
#--------------- Saving sorted data -------------------------------------------
    input_data[column] = sorted_data
#----------------- Printing processing times ----------------------------------
    print(f"Execution time for non-decreasing merge sort of {column}: {processing_time} seconds")


#----------------- Saving sorted data to file ---------------------------------
input_data.to_csv("merge_nonInc.csv", index=False)


#------Plotting execution time graphs ------------------------------------------

categories = list(proc_time.keys())
times= list(proc_time.values())

plt.bar(categories,times)
plt.xlabel('Categories')
plt.ylabel('Time')
plt.title('Execution of Merge sort Non-increasing Order')

plt.show()
