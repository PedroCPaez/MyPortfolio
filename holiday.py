# T16 - Programming with User Defined Functions

from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def get_coordinates(place_name):
    # Finds coordinates between cities to fly, to calculate a flight base price.
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(place_name)
    
    if location:
        return location.latitude, location.longitude
    else:
        print(f"We couldn't find the location for {place_name}")
        return None


def calculate_distance(place_one, place_two):
    # Calculates distance between cities to fly, to calculate a flight base price.
    coord_one = get_coordinates(place_one)
    coord_two = get_coordinates(place_two)

    if coord_one and coord_two:
        distance = geodesic(coord_one, coord_two).kilometers
        return distance
    else:
        return None


def get_number_of_travelers():
    # Gets number of travelers, to calculate a flight base price.
    try:
        num_travelers = int(input("\nHow many people will be traveling?: "))
        return num_travelers
    except ValueError:
        print("\033[91mPlease enter a valid number.\033[0m")
        return get_number_of_travelers()


def get_valid_positive_integer_input(prompt):
    # Validates entry data from user.
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("\033[91mPlease enter a positive integer.\033[0m")
        except ValueError:
            print("\033[91mPlease enter a valid number.\033[0m")


def calculate_accommodation_cost(num_people, num_nights):
    # Approx. Accommodation cost in a 5* hotel.
    hotel_base_cost_per_person = 50
    return hotel_base_cost_per_person * num_people * num_nights


def calculate_car_rental_cost(num_cars, num_days, car_size):
    # Approx. Car rental cost depending on size car.
    compact_price_per_day = 30
    suv_price_per_day = 50

    # Dictionary used to validate user's choice.
    car_prices = {"Compact": compact_price_per_day, "Suv": suv_price_per_day}

    # Validates if user's choice is in the dictionary and calculates base price.
    if car_size.capitalize() in car_prices:
        rental_base_price_per_day = car_prices[car_size.capitalize()]
        return rental_base_price_per_day * num_cars * num_days
    else:
        print("\033[91mInvalid car size. Please choose 'Compact' or 'Suv'.\033[0m")
        return None


def get_valid_location_input(prompt):
    # Validates data entry from the user (cities of origin and destiny).
    while True:
        place = input(prompt)
        if place.strip() and all(word.isalpha() for word in place.split()):
            return place.title()
        else:
            print("\033[91mPlease enter a valid location with letters only.\033[0m")


def get_output_file(result):
    # Generates an historical file adding the obtained data result,
    # depending on data entered by the user.
    file_name = "holidays.txt"
    with open(file_name, "a+", encoding="utf-8") as file:
        file.write(result)
    print(f"\n\033[92mResults have been written to {file_name}\033[0m\t"
          f"\033[92mHappy holidays!\033[0m\n")


def start_and_end_line():
    # Separator line between records.
    print("*-" * 50)


def main():
    # Main code, starting to get data from user and calculate costs.
    place_one = get_valid_location_input("\nWhich city or place are you flying from?: ")
    place_two = get_valid_location_input("\nWhich city or place are you flying to?: ")
    distance = calculate_distance(place_one, place_two)

    if distance is not None:
        num_travelers = get_number_of_travelers()

        # Base flight cost, depending on the distance between cities.
        if distance < 3000:
            base_price = 20
        elif distance < 5000:
            base_price = 100
        elif distance < 7000:
            base_price = 300
        else:
            base_price = 1000

        # Calculates approx. Round flight cost.
        flights_cost = base_price * num_travelers * 2  # (by 2) as round trip.

        # Get number of nights and calculate accommodation cost.
        num_nights = get_valid_positive_integer_input("\nHow many nights will you be staying?: ")
        accommodation_cost = calculate_accommodation_cost(num_travelers, num_nights)

        # Get data from user and calculates approx. Car rental cost.
        num_cars = get_valid_positive_integer_input("\nHow many cars would you like to rent?: ")
        num_days = get_valid_positive_integer_input("\nHow many days would you like to rent the cars?: ")
        car_size = input("\nWhat size car would you like to rent? (Compact/Suv): ")

        car_rental_cost = calculate_car_rental_cost(num_cars, num_days, car_size)

        if car_rental_cost is not None:
            # Calculates total holidays cost.
            total_holidays_cost = flights_cost + accommodation_cost + car_rental_cost

            # Prints results on the terminal.
            start_and_end_line()
            print(f"\n\033[93mThe cost per {num_travelers} round flights "
                  f"{place_one} - {place_two} - {place_one} is £{flights_cost:.2f}, "
                  "booking up to 4 weeks in advance.\n\033[0m")
            print(f"\n\033[93mThe accommodation cost per {num_travelers} person/people "
                  f"per {num_nights} nights "
                  f"is £{accommodation_cost:.2f}, unless high season.\n\033[0m")
            print(f"\n\033[93mThe rent cost per {num_cars} {car_size.capitalize()} car/s "
                  f"per {num_days} days is £{car_rental_cost:.2f}.\033[0m")
            print(f"\n\n\033[92mThe total cost including flights, accommodation and "
                  f"car rental is £{total_holidays_cost:.2f}.\n\033[0m")
            start_and_end_line()
            
            # Generates output file's display.
            result = "*-" * 50 + "\n"
            result += (
                f"The cost per {num_travelers} round flights {place_one} "
                f"- {place_two} - {place_one} is £{flights_cost:.2f}, "
                f"booking up to 4 weeks in advance.\n"
                )
            result += (
                f"The accommodation cost per {num_travelers} person/people "
                f"per {num_nights} nights is £{accommodation_cost:.2f}, "
                f"unless high season.\n"
                )
            result += (
                f"The total cost per {num_cars} {car_size.capitalize()} car/s "
                f"per {num_days} days is £{car_rental_cost:.2f}.\n"
            )
            result += (
                f"\nThe grand total including flights, accommodation, and car rental "
                f"is £{total_holidays_cost:.2f}.\n"
            )

            # Get the output file, with the resulting data.
            get_output_file(result)


if __name__ == "__main__":
    main()
