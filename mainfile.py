# Open up CSV File

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("Fantasy_Football_Projections_RB.csv")

# Print DF
print(df)

# Group data by team and FPTS


# Get description
descriptioncsv = df.describe()
print(descriptioncsv)
