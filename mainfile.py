import pandas as pd
import matplotlib.pyplot as plt


file_name = "Fantasy_Football_Projections_RB.csv"


# Read CSV
def csv_open(file_path):
    data = pd.read_csv(file_path)
    return data


def groupsorted_data(dataframe):
    # Group data by team and FPTS
    grouped = pd.DataFrame(dataframe.groupby("Team")["FPTS"].sum()).reset_index(
        drop=False
    )

    # Sort the new dataframe in ascending order
    grouped = grouped.sort_values(by="FPTS", ascending=True)
    return grouped


def summary_stat(dataframe):
    # Get summary statistics
    description = dataframe.describe()
    return description


# Creating bar chart
def bar_chart(dataframe):
    # Setting x to nfl team column and y to fantasy points column
    x = dataframe["Team"]
    y = dataframe["FPTS"]

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
def scatterplot(dataframe):
    # Setting x to nfl team column and y to fantasy points column
    x = dataframe["Team"]
    y = dataframe["FPTS"]

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
dataframe = csv_open(file_name)

# Group data
grouped_df = groupsorted_data(dataframe)
print(grouped_df)

# Print stats summary
descriptioncsv = summary_stat(grouped_df)
print(descriptioncsv)

# Bar chart
bar_chart(grouped_df)

# Scatterplot
scatterplot(grouped_df)
