# Initialize an empty dictionary to store airport data
airport_data = {}

# Function to add a new airport to the dictionary
def add_airport():
    icao_code = input("Enter the ICAO code of the airport: ").strip().upper()
    airport_name = input("Enter the name of the airport: ")
    airport_data[icao_code] = airport_name
    print(f"Airport {icao_code} ({airport_name}) added successfully!")

# Function to fetch airport information
def fetch_airport_info():
    icao_code = input("Enter the ICAO code of the airport you want to fetch: ").strip().upper()
    if icao_code in airport_data:
        print(f"Airport {icao_code}: {airport_data[icao_code]}")
    else:
        print(f"Airport with ICAO code {icao_code} not found.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Please choose an option (1/2/3): ").strip()

    if choice == '1':
        add_airport()
    elif choice == '2':
        fetch_airport_info()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3).")









