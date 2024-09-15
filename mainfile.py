import pandas as pd
import matplotlib.pyplot as plt


file_name = "Fantasy_Football_Projections_RB.csv"


# Read CSV
def csv_open(file_path):
    df = pd.read_csv(file_path)
    return df


def groupsorted_data(dataframe):
    # Group data by team and FPTS
    grouped_df = pd.DataFrame(dataframe.groupby("Team")["FPTS"].sum()).reset_index(
        drop=False
    )

    # Sort the new dataframe in ascending order
    grouped_df = grouped_df.sort_values(by="FPTS", ascending=True)
    return grouped_df


def summary_stat(dataframe):
    # Get summary statistics
    description = dataframe.describe()
    return description


# Creating bar chart
def bar_chart(grouped_df):
    # Setting x to nfl team column and y to fantasy points column
    x = grouped_df["Team"]
    y = grouped_df["FPTS"]

    # Plotting the bar chart
    plt.bar(x, y, width=0.8, color="orange")

    # Rotating all x-axis labels vertically to fit on the chart
    plt.xticks(range(len(x)), x, rotation="vertical")

    # Labeling the chart
    plt.title("Projected Total RB Fantasy Football Points By NFL Team")
    plt.xlabel("NFL Team")
    plt.ylabel("Running Backs Total Fantasy Football Points 2024")

    # Show the chart
    plt.show()


# Create Scatterplot
def scatterplot(grouped_df):
    # Setting x to nfl team column and y to fantasy points column
    x = grouped_df["Team"]
    y = grouped_df["FPTS"]

    # Plotting the scatter chart
    plt.scatter(x, y, color="orange")

    # Rotating all x-axis labels vertically to fit on the chart
    plt.xticks(range(len(x)), x, rotation="vertical")

    # Labeling the chart
    plt.title("Projected Total RB Fantasy Football Points By NFL Team")
    plt.xlabel("NFL Team")
    plt.ylabel("Running Backs Total Fantasy Football Points 2024")

    # Show the chart
    plt.show()


# Csv open
df = csv_open(file_name)

# Group data
grouped_df = groupsorted_data(df)
print(grouped_df)

# Print stats summary
descriptioncsv = summary_stat(grouped_df)
print(descriptioncsv)

# Bar chart
bar_chart(grouped_df)

# Scatterplot
scatterplot(grouped_df)
