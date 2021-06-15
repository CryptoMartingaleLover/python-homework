#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Playing with PyBank and trying to get it all to work/


# In[ ]:


'''
This code will analyze the financial records of a company. It is a very simple data set comprised of date and profit/loss 
for each date. 

It will calculate:
    - The total number of months included in the dataset.
    - The net total amount of Profit/Losses over the entire period.
    - The average of the changes in Profit/Losses over the entire period.
    - The greatest increase in profits (date and amount) over the entire period.
    - The greatest decrease in losses (date and amount) over the entire period.
    
Target results should look similar to this:

Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''


# In[ ]:





# In[1]:


# Import the necessary libraries for reading CSV files.
import os
import csv


# In[ ]:





# In[2]:


#  Set the path for the CSV file.

from pathlib import Path


# In[ ]:





# In[3]:


Path.cwd()


# In[ ]:





# In[4]:


budget_data_path = Path('budget_data.csv')


# In[5]:


# Create an empty list to hold dates. Create an empty list to hold daily profit/loss.

date_list = []
pnl_list = []
full_list = []



# In[14]:


# Open the CSV file.

with open (budget_data_path, "r") as budget_data_file:
    csv_reader = csv.reader(budget_data_file, delimiter = ',')
    header = next(csv_reader)
        
    for line in csv_reader:
        date = line[0]
        day_to_day_profit_loss = int(line[1])
        
        date_list.append(date)
        pnl_list.append(day_to_day_profit_loss)
        
        full_list.insert(0, date_list)
        full_list.insert(1, pnl_list)
        
        
        print(f"Date: {date} - Profit/Loss: ${day_to_day_profit_loss}")
        


# In[ ]:





# In[7]:


# Initialize metric variables

greatest_profit = 0          # Highest daily profit.
greatest_loss = 0            # Lowest daily loss.
avg_change_profit_loss = 0   # Average of the sum of daily changes - alternatively the difference of 1st & last values divided by total months.
net_profit_loss = 0          # The sum of profit line. 
count_months = 0             # Total count of months in data set.


# In[8]:


# Calculate the net_profit_loss, hightest daily profit, lowest daily loss
for day_to_day_profit_loss in pnl_list:
        
    # Sum the total and count variables
    net_profit_loss += int(day_to_day_profit_loss)
    count_months += 1
    
    
    # Logic to determine highest daily profit and lowest daily loss
    if greatest_loss == 0:
        greatest_loss = day_to_day_profit_loss
    elif int(day_to_day_profit_loss) > int(greatest_profit):
        greatest_profit = int(day_to_day_profit_loss)
    elif int(day_to_day_profit_loss) < int(greatest_loss):
        greatest_loss = int(day_to_day_profit_loss)


# In[9]:


print(greatest_profit, greatest_loss, net_profit_loss, (count_months-1))


# In[36]:


for month in date_list[:]:
    current_month = date
    current_pl = day_to_day_profit_loss
    
print(month)


# In[35]:


print(date_list)


# In[ ]:





# In[ ]:





# In[39]:


for index, item in enumerate(date_list):
    print('Index ' + str(index) + ' in date list is: ' + item)
   


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[74]:


print(f"Greatest Increase in Profits: {full_list[0]} (${full_list[1]})") # This format is 100% correct, but wrong date and profit/loss.


# In[41]:


budget_data_dict = {}

with open(budget_data_path, mode='r') as inp:
    reader = csv.reader(inp)
    budget_data_dict = {rows[0]:rows[1] for rows in reader}


# In[42]:


# Getting it in Print.

print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {count_months}')
print(f'Total Net Profit/Loss: ${net_profit_loss}')
avg_change_profit_loss = round((pnl_list[-1] - pnl_list[0])/(count_months-1), 2)  
print(f'Average Daily Change: ${avg_change_profit_loss}')
# Print out dict key-value pairs
for key, value in budget_data_dict.items():
    if value == str(greatest_profit):
        print(f"Greatest Increase in Profits: {key} (${value})")
for key, value in budget_data_dict.items():
    if value == str(greatest_loss):
        print(f"Greatest Decrease in Profits: {key} (${value})")
print()


# In[ ]:





# In[63]:


import sys
sys.stdout = open('HWOutput.txt','wt')
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {count_months}')
print(f'Total Net Profit/Loss: ${net_profit_loss}')
avg_change_profit_loss = round((pnl_list[-1] - pnl_list[0])/(count_months-1), 2)  
print(f'Average Daily Change: ${avg_change_profit_loss}')
# Print out dict key-value pairs
for key, value in budget_data_dict.items():
    if value == str(greatest_profit):
        print(f"Greatest Increase in Profits: {key} (${value})")
for key, value in budget_data_dict.items():
    if value == str(greatest_loss):
        print(f"Greatest Decrease in Profits: {key} (${value})")
print()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




