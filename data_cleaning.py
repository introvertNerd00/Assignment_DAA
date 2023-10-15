import pandas as pd

def clean_data(data):
    #  Select columns for processing
    columns_required = [
        'Current Loan Amount', 'Credit Score', 'Annual Income', 'Monthly Debt',
        'Years of Credit History', 'Months since last delinquent', 'Number of Open Accounts',
        'Number of Credit Problems', 'Current Credit Balance', 'Maximum Open Credit',
        'Bankruptcies', 'Tax Liens'
    ]

    if 'Monthly Debt' in columns_required:
        data['Monthly Debt'] = data['Monthly Debt'].str.replace('[\$,]', '', regex=True)

    for column in columns_required:
        data[column] = pd.to_numeric(data[column], errors='coerce')

    medians = data[columns_required].median()

    for column in columns_required:
        data[column].fillna(medians[column], inplace=True)

    
    data.to_csv("clean_data.csv", index=False)

if __name__ == "__main__":
    # Read the original CSV file into a DataFrame
    df = pd.read_csv("Dataset.csv")

    # Perform preprocessing
    cleaned_data = clean_data(df)
