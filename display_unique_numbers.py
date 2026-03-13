def display_unique_numbers():
    number_list = []
    
    for i in range(10):
        user_input = float(input(f"Enter number {i+1}: "))
        number_list.append(user_input)
    
    print("\nNumbers that don't have duplicates:")
    for num in number_list:
        if number_list.count(num) == 1:
            print(num)

if __name__ == "__main__":
    display_unique_numbers()