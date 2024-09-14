# Open up CSV File

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("Fantasy_Football_Projections_RB.csv")

# Print DF
# print(df)

# Group data by team and FPTS
new_df = pd.DataFrame(df.groupby("Team")["FPTS"].sum()).reset_index(drop=False)

# Make the new df sort by aesending order
new_df = new_df.sort_values(by="FPTS", ascending=True)

print(new_df)


# Get summary statistics
descriptioncsv = new_df.describe()
print(descriptioncsv)
print(new_df)

# Creating bar chart
# Setting x to nfl team column and y to fantasy points column
x = new_df["Team"]
y = new_df["FPTS"]
# Plotting the  bar chart
plt.bar(x, y, width=0.8, color="orange")
# Rotating all x-axis labels vertically that way they fit on the chart
plt.xticks(range(len(x)), x, rotation="vertical")
# Labeling chart
plt.title("Projected Total RB Fantasy Football Points By NFL Team")
plt.xlabel("NFL Team")
plt.ylabel("Running Backs Total Fantasy Football Points 2024")
# Show the chart
plt.show()
