city_air = {
    "London": 6.5,
    "Cardiff": 5.3,
    "Edinburgh": 4.6,
    "Belfast": 5.0
}

def display_all_data():
    # If no data, inform the user
    if not city_air:
        print("No city data available.\n")
        return

    # Print header
    print(f"{'City':<15} {'AQI':>6}")
    print("-" * 22)

    # Loop through dictionary items and print each
    for city, aqi in city_air.items():
        print(f"{city:<15} {aqi:6.2f}")
    print()

def add_aqi_data():
    # Read city name from user and strip whitespace
    city = input("Enter city name (or leave blank to cancel): ").strip()
    if not city:
        print("Add cancelled.\n")
        return

    # If city exists, ask whether to overwrite
    if city in city_air:
        resp = input(f"{city} exists (AQI={city_air[city]:.2f}). Overwrite? (y/N): ").strip().lower()
        if resp != "y":
            print("Not overwritten.\n")
            return

    # Read AQI value and validate numeric input
    aqi_str = input(f"Enter AQI value for {city}: ").strip()
    try:
        aqi_value = float(aqi_str)
    except ValueError:
        print("Invalid AQI. Please enter a numeric value.\n")
        return

    # Store value in dictionary (assignment operator used)
    city_air[city] = aqi_value
    print(f"{city} added/updated with AQI = {aqi_value:.2f}\n")

def search_city_aqi():
    # Read search query
    query = input("Enter city name to search: ").strip()
    if not query:
        print("Search cancelled.\n")
        return

    # Loop through keys and compare lowercased names for case-insensitive match
    for city in city_air:
        if city.lower() == query.lower():
            print(f"Found: {city} -> AQI = {city_air[city]:.2f}\n")
            return

    # If loop completes without return, city not found
    print(f"City '{query}' not found in data.\n")

def display_menu():
    print("AQI Menu")
    print("1. Display all data")
    print("2. Add city AQI")
    print("3. Search city AQI")
    print("4. Exit")

def run_aqi_system():
    print("Starting with pre-loaded city AQI data.\n")
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        # Use conditional branching to run the correct function (1-4)
        if choice == "1":
            display_all_data()
        elif choice == "2":
            add_aqi_data()
        elif choice == "3":
            search_city_aqi()
        elif choice == "4":
            print("Exiting. Goodbye.")
            break
        else:
            print("Invalid choice. Enter 1-4.\n")
            
