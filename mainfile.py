# Open up CSV File

import pandas as pd
import matplotlib.pyplot as plt


file_name = "Fantasy_Football_Projections_RB.csv"


# Read CSV
def csv_open(file_name):
    df = pd.read_csv(file_name)
    return df


def groupsorted_data(df):
    # Group data by team and FPTS
    new_df = pd.DataFrame(df.groupby("Team")["FPTS"].sum()).reset_index(drop=False)

    # Make the new df sort by aesending order
    new_df = new_df.sort_values(by="FPTS", ascending=True)
    return new_df


# print(new_df)


def summary_stat(df):
    # Get summary statistics
    descriptioncsv = df.describe()
    # print(descriptioncsv)
    # print(df)
    return descriptioncsv


# Creating bar chart
def bar_chart(df):
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


# Create Scatterplot
def scatterplot(df):
    # Setting x to nfl team column and y to fantasy points column
    x = new_df["Team"]
    y = new_df["FPTS"]
    # Plotting the scatter chart
    plt.scatter(x, y, color="orange")
    # Rotating all x-axis labels vertically that way they fit on the chart
    plt.xticks(range(len(x)), x, rotation="vertical")
    # Labeling chart
    plt.title("Projected Total RB Fantasy Football Points By NFL Team")
    plt.xlabel("NFL Team")
    plt.ylabel("Running Backs Total Fantasy Football Points 2024")
    # Show the chart
    plt.show()


# Csv open
df = csv_open(file_name)

# Group data
new_df = groupsorted_data(df)
print(new_df)

# print stats summary
descriptioncsv = summary_stat(new_df)
print(descriptioncsv)

# bar chart
bar_chart(new_df)

# scatterplot
scatterplot(df)
