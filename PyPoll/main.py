# %%
import pandas as pd
from pathlib import Path

# %%
# To read the csv File
election_file = "Resources/election_data.csv"
election_file_df = pd.read_csv(election_file)

# Statistical Overview of data
election_file_df.describe()

# %%
# first 5 rows
election_file_df.head()

# %%
# Number of columns in data set
election_file_df.columns

# %%
# Declaring Variables

county = election_file_df["County"]
candidates = election_file_df["Candidate"]
Charles = []
Raymond = []
Diana = []

# Looping through rows



 # Vote Count
total_votes = (len(candidates))
print(total_votes)
 
 # Votes by Person 
for candidate in candidates:
   
   if candidate == "Charles Casper Stockham":
     Charles.append(candidates)
     Charles_votes = len(Charles)
   elif candidate == "Raymon Anthony Doane":
     Raymond.append(candidates)
     Raymond_votes = len(Raymond)
   else:
     Diana.append(candidates)
     Diana_votes = len(Diana)
print(Charles_votes)
print(Raymond_votes)
print(Diana_votes)

 # Percent Votes
Charles_percent =round(((Charles_votes / total_votes) *100), 2)
Raymond_percent =round(((Raymond_votes / total_votes) *100), 2)
Diana_percent =round(((Diana_votes / total_votes) *100), 2)
print(Charles_percent)
print(Raymond_percent)
print(Diana_percent)

 # Winner
if Charles_percent > max(Raymond_percent, Diana_percent):
     winner = "Charles"
elif Raymond_percent > max(Charles_percent, Diana_percent):
     winner = "Raymond"
else:
    winner = "Diana"

    # Print Statement
print(f"Election Results \n") 
print(f"...................\n") 
print(f' Total Votes: {total_votes}\n') 
print(f"Charles: {Charles_percent}% ({Charles_votes})\n") 
print(f"Raymond: {Raymond_percent}% ({Raymond_votes})\n") 
print(f"Diana: {Diana_percent}% ({Diana_votes})\n") 
print(f"Winner: {winner}\n") 



# %%



