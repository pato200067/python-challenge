# %%
import pandas as pd
from pathlib import Path

# %%
# To Read The csv File
budget_file =  "Resources/budget_data.csv"
budget_file_df =pd.read_csv(budget_file)

# %%
# Statistical Analysis of Data Set
budget_file_df.describe()


# %%
# Columns In Data Set
budget_file_df.columns

# %%
# Total Number Of Months Included In The Data Set
total_months = budget_file_df["Date"].count()
# Net Total Amount of Profit/Losses
net_total = budget_file_df["Profit/Losses"].sum()
# Calculate Monthly Changes in Profits
# Create List To Store Data
profit = []
monthly_changes = []
date = []
# Initialize THe Variable as Required
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
# Iterate through each row in the Dataframe
for index, row in budget_file_df.iterrows():
    # Count will count the number of months in the data set
    count += 1
    # Needed when collecting the greatest increase and decrease in profits
    date.append(row["Date"])
    profit.append(row["Profit/Losses"])
    total_profit += int(row["Profit/Losses"])

    #Calculate the average change in profits from month to month
    final_profit = int(row["Profit/Losses"])
    monthly_change_profits = final_profit - initial_profit

    # Store monthly changes in a list
    monthly_changes.append(monthly_change_profits)
    total_change_profits += monthly_change_profits

    initial_profit = final_profit

 # Calculate the average change in profits
average_change_profits = total_change_profits / (count - 1)

# Find the max and min change in profit 
greatest_increase_profits = max(monthly_changes)
greatest_decrease_profits = min(monthly_changes)
increase_date = date[monthly_changes.index(greatest_increase_profits)]
decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

print(".................")
print("Financial Analysis")
print(f"Total Months: {str(count)}")
print(f"Total Profits: ${str(total_profit)}")
print(f"Average Change: ${str(round(average_change_profits, 2))}")
print(f"Greatest Increase in Profits: {increase_date} (${str(greatest_increase_profits)})")
print(f"Greatest Decrease in Profits: {decrease_date} (${str(greatest_decrease_profits)})")





