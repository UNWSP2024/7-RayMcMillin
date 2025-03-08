# Ray McMillin, 3/7/25, Rainfall Code

def main():
    
    rainfall = []
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    for month in months:
        while True:
            try:
                amount = float(input(f"Enter the total rainfall for {month}: "))
                if amount < 0:
                    print("The amount of rainfall for a month cannot be below zero. Please enter a valid integer. If there was no rainfall, simply input 0.")
                else:
                    rainfall.append(amount)
                    break
            except ValueError:
                print("Error. Please enter a valid numerical digit.")
    
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / len(rainfall)
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]
    
    print(f"\nTotal rainfall for the year: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Month with the highest rainfall: {max_month} ({max_rainfall:.2f} inches)")
    print(f"Month with the lowest rainfall: {min_month} ({min_rainfall:.2f} inches)")

if __name__ == "__main__":
    main()
