# Sample data for Atlantis population (instead of reading from file)
data = [
    {'year': 2000, 'population': 1000},
    {'year': 2001, 'population': 1050},
    {'year': 2002, 'population': 1100},
    {'year': 2003, 'population': 1150},
    {'year': 2004, 'population': 1200},
    {'year': 2005, 'population': 1250},
    {'year': 2006, 'population': 1300},
    {'year': 2007, 'population': 1350},
    {'year': 2008, 'population': 1400},
    {'year': 2009, 'population': 1450},
    {'year': 2010, 'population': 1500},
]

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
            years = [d['year'] for d in data]
            if year in years:
                pop = next(d['population'] for d in data if d['year'] == year)
                print(f"Population in {year}: {pop}")
            else:
                print("Year not found in data.")
        except ValueError:
            print("Invalid year. Please enter a number.")

    elif choice == '2':
        try:
            start_year = int(input("Enter start year: "))
            end_year = int(input("Enter end year: "))
            years = [d['year'] for d in data]
            if start_year in years and end_year in years:
                start_pop = next(d['population'] for d in data if d['year'] == start_year)
                end_pop = next(d['population'] for d in data if d['year'] == end_year)
                growth = (end_pop - start_pop) / start_pop * 100
                print(f"Growth rate from {start_year} to {end_year}: {growth:.2f}%")
            else:
                print("One or both years not found in data.")
        except ValueError:
            print("Invalid years. Please enter numbers.")

    elif choice == '3':
        populations = [d['population'] for d in data]
        total_years = len(data)
        avg_population = sum(populations) / len(populations)
        max_population = max(populations)
        min_population = min(populations)
        overall_growth = (populations[-1] - populations[0]) / populations[0] * 100
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