def check_duplicate_on_input():
    history_of_numbers = []
    
    while True:
        user_entry = input("Enter a number (or any letter to stop): ")
        
        try:
            current_number = float(user_entry)
            if current_number in history_of_numbers:
                print("Duplicate")
            else:
                print("Unique")
                history_of_numbers.append(current_number)
        except ValueError:
            print("Invalid input detected. Stopping program.")
            break

if __name__ == "__main__":
    check_duplicate_on_input()