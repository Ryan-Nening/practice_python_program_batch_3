def display_first_occurrences():
    input_numbers = []
    seen_numbers = []
    
    for i in range(10):
        num = float(input(f"Enter number {i+1}: "))
        input_numbers.append(num)
        
    print("\nDisplaying numbers (duplicates shown only once):")
    for num in input_numbers:
        if num not in seen_numbers:
            print(num)
            seen_numbers.append(num)

if __name__ == "__main__":
    display_first_occurrences()