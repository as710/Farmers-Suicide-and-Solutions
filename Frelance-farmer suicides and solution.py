#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Frelance_ farmer suicides and soltion in India.


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data Collection and Analysis
data = {
    "year": list(range(2011, 2021)),
    "farmer_suicides": [12000, 12250, 12500, 12750, 13000, 13250, 13500, 13750, 14000, 14250],
    "crop_failure_rate": [15, 17, 18, 16, 19, 21, 20, 22, 23, 25],
    "loan_amount": [45000, 47000, 49000, 51000, 53000, 55000, 57000, 59000, 61000, 63000],
    "market_price_index": [100, 97, 95, 93, 91, 89, 87, 85, 83, 81]
}

df = pd.DataFrame(data)

# Visualizing the data
def visualize_data(df):
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Farmer Suicides Over the Years
    axs[0, 0].plot(df['year'], df['farmer_suicides'], marker='o', color='r')
    axs[0, 0].set_title('Farmer Suicides Over the Years')
    axs[0, 0].set_xlabel('Year')
    axs[0, 0].set_ylabel('Number of Suicides')

    # Crop Failure Rate Over the Years
    axs[0, 1].plot(df['year'], df['crop_failure_rate'], marker='o', color='g')
    axs[0, 1].set_title('Crop Failure Rate Over the Years')
    axs[0, 1].set_xlabel('Year')
    axs[0, 1].set_ylabel('Crop Failure Rate (%)')

    # Loan Amount Over the Years
    axs[1, 0].plot(df['year'], df['loan_amount'], marker='o', color='b')
    axs[1, 0].set_title('Loan Amount Over the Years')
    axs[1, 0].set_xlabel('Year')
    axs[1, 0].set_ylabel('Average Loan Amount (INR)')

    # Market Price Index Over the Years
    axs[1, 1].plot(df['year'], df['market_price_index'], marker='o', color='purple')
    axs[1, 1].set_title('Market Price Index Over the Years')
    axs[1, 1].set_xlabel('Year')
    axs[1, 1].set_ylabel('Market Price Index')

    plt.tight_layout()
    plt.show()

def identify_critical_years(df):
    critical_years = df[(df['farmer_suicides'] > 13000) & (df['crop_failure_rate'] > 20)]
    return critical_years

# Propose solutions based on critical years
def propose_solutions(critical_years):
    solutions = []
    if not critical_years.empty:
        solutions.append("Implement debt relief programs focusing on the identified critical years to reduce financial stress.")
        solutions.append("Expand crop insurance coverage to ensure timely compensation for crop failures during these critical years.")
        solutions.append("Stabilize market prices by introducing MSPs and improving market access, particularly for the critical years.")
        solutions.append("Establish mental health support programs in regions most affected during these critical years.")
        solutions.append("Invest in irrigation and storage facilities to mitigate the impacts of crop failures and improve resilience.")
    return solutions

def main():
    print("Data Collection and Analysis")
    print(df)
    
    print("\nVisualizing Data")
    visualize_data(df)
    
    print("\nIdentifying Critical Years")
    critical_years = identify_critical_years(df)
    print(critical_years)
    
    print("\nProposing Solutions")
    solutions = propose_solutions(critical_years)
    for solution in solutions:
        print("- " + solution)

if __name__ == "__main__":
    main()


# In[ ]:




