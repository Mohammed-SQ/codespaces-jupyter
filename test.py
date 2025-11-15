import pandas as pd

# Load the data
df = pd.read_csv('data/atlantis.csv')

print("Welcome to Atlantis Population Analyzer!")

while True:
    print("\nOptions:")
    print("1. Get population for a specific year")
    print("2. Calculate growth rate between two years")
    print("3. Show overall statistics")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        try:
            year = int(input("Enter the year: "))
            if year in df['year'].values:
                pop = df[df['year'] == year]['population'].values[0]
                print(f"Population in {year}: {pop}")
            else:
                print("Year not found in data.")
        except ValueError:
            print("Invalid year. Please enter a number.")

    elif choice == '2':
        try:
            start_year = int(input("Enter start year: "))
            end_year = int(input("Enter end year: "))
            if start_year in df['year'].values and end_year in df['year'].values:
                start_pop = df[df['year'] == start_year]['population'].values[0]
                end_pop = df[df['year'] == end_year]['population'].values[0]
                growth = (end_pop - start_pop) / start_pop * 100
                print(f"Growth rate from {start_year} to {end_year}: {growth:.2f}%")
            else:
                print("One or both years not found in data.")
        except ValueError:
            print("Invalid years. Please enter numbers.")

    elif choice == '3':
        total_years = len(df)
        avg_population = df['population'].mean()
        max_population = df['population'].max()
        min_population = df['population'].min()
        overall_growth = (df['population'].iloc[-1] - df['population'].iloc[0]) / df['population'].iloc[0] * 100
        print(f"Total years: {total_years}")
        print(f"Average population: {avg_population:.0f}")
        print(f"Maximum population: {max_population}")
        print(f"Minimum population: {min_population}")
        print(f"Overall growth rate: {overall_growth:.2f}%")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")