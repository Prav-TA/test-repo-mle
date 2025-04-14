import pandas as pd


def main():
    """
    Calculate % of U.S. residents living in highly walkable neighborhoods.
    """
    csv_file = "EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv"
    highly_walkable = 15.26

    df = pd.read_csv(csv_file)
    total_population = df["TotPop"].sum()
    highly_walkable_pop = df[df["NatWalkInd"] >= highly_walkable]["TotPop"].sum()
    percentage = (highly_walkable_pop / total_population) * 100.0

    print(f"{percentage:.2f}% of U.S. residents live in highly walkable neighborhoods.")


if __name__ == "__main__":
    main()
