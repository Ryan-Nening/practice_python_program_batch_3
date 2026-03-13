def find_minimum_value():
    lowest_number = None
    
    while True:
        entry = input("Enter a number (or any letter to stop): ")
        
        try:
            val = float(entry)
            if lowest_number is None or val < lowest_number:
                lowest_number = val
        except ValueError:
            break
            
    if lowest_number is not None:
        print(f"The lowest number entered was: {lowest_number}")
    else:
        print("No valid numbers were entered.")

if __name__ == "__main__":
    find_minimum_value()