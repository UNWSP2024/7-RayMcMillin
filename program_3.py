# Ray McMillin, 3/7/25, US Population

def main():
    all_entered_values = []
    while True:
        try:
            year = int(input("Enter year (or -1 to stop): "))
            if year == -1:
                break
            state = input("Enter state name: ")
            population = int(input("Enter population: "))
            all_entered_values.append([year, state, population])  
        except ValueError:
            print("Invalid input. Please enter valid values for the year and population.")
    
    return all_entered_values 

def sum_population_for_year(all_entered_values, year_to_sum):
    total_population = sum(entry[2] for entry in all_entered_values if entry[0] == year_to_sum)  
    return total_population

if __name__ == '__main__':
    state_data = main()  

    search_year = int(input("Enter a year to find total population: "))
    total_population = sum_population_for_year(state_data, search_year)

    print(f"Total population for the year {search_year}: {total_population}")
