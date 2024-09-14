from mainfile import groupsorted_data
from mainfile import csv_open
from mainfile import summary_stat
from mainfile import bar_chart
from mainfile import scatterplot

import pandas as pd
from io import StringIO

df_test = pd.DataFrame(
    {
        "Team": ["TeamA", "TeamB", "TeamA", "TeamC", "TeamB"],
        "FPTS": [120, 200, 150, 90, 50],
    }
)


def test_csv_open():
    # Sample CSV data for testing
    sample_data = {"Team": ["TeamA", "TeamB", "TeamC"], "FPTS": [120, 200, 90]}

    # Create expected DataFrame
    expected_output = pd.DataFrame(sample_data)

    # Mock CSV file creation (could be done using a file or testing framework)
    test_file = "test_file.csv"
    expected_output.to_csv(test_file, index=False)

    # Run the function to test
    result = csv_open(test_file)

    # Assert DataFrame equality
    assert result.equals(
        expected_output
    ), f"Test Failed. Expected: \n{expected_output}\nGot: \n{result}"


# Test the grouping and sorting function
def test_groupsorted_data():
    # Expected DataFrame after grouping and sorting
    expected_output = pd.DataFrame(
        {
            "Team": ["TeamC", "TeamB", "TeamA"],
            "FPTS": [90, 250, 270],
        }
    ).reset_index(drop=True)

    result = groupsorted_data(df_test).reset_index(drop=True)

    # Check if the output matches the expected result
    assert result.equals(
        expected_output
    ), f"Test Failed. Expected: \n{expected_output}\nGot: \n{result}"


def test_summary_stat():
    # Input DataFrame for testing
    df_test = pd.DataFrame(
        {"Team": ["TeamC", "TeamB", "TeamA"], "FPTS": [90, 250, 270]}
    )

    # Expected summary statistics for "FPTS"
    expected_summary = pd.DataFrame(
        {"FPTS": [3, 203.33, 98.66, 90, 170, 250, 260, 270]},
        index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"],
    )

    # Run the function to test
    result = summary_stat(df_test)

    # Extract only the FPTS statistics from result
    result_fpts = result["FPTS"]

    # Assert that the statistics match with a relative tolerance for floating-point differences
    pd.testing.assert_series_equal(result_fpts, expected_summary["FPTS"], rtol=1e-2)


def test_bar_chart():
    # Define the dummy DataFrame directly inside the function
    csv_data = """Team,FPTS
                  Team A,200
                  Team B,150
                  Team C,300"""

    df = pd.read_csv(StringIO(csv_data))

    try:
        # Test bar_chart without displaying the plot
        bar_chart(df)
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Bar chart failed: {e}")

    assert plot_success, "Bar chart generation failed"


def test_scatterplot():
    # Define the dummy DataFrame directly inside the function
    csv_data = """Team,FPTS
                  Team A,200
                  Team B,150
                  Team C,300"""

    df = pd.read_csv(StringIO(csv_data))

    try:
        # Test scatterplot without displaying the plot
        scatterplot(df)
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Scatterplot failed: {e}")

    assert plot_success, "Scatter plot generation failed"


if __name__ == "__mainfile___":
    test_csv_open()
    test_groupsorted_data()
    test_summary_stat()
    test_bar_chart()
    test_scatterplot()
