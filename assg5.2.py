#________________________________________________________________________________________
largest_num = None
smallest_num = None

while True:
    user_input = input("Enter a number (or 'done' to exit): ")

    if user_input.lower() == "done":
        break  # Exit the loop cleanly

    try:
        num = int(user_input)

        # If it's the first number, it is both the largest and smallest
        if largest_num is None or num > largest_num:
            largest_num = num
        if smallest_num is None or num < smallest_num:
            smallest_num = num

    except ValueError:
        print("Invalid input. Please enter a valid integer or 'done'.")

# Only print results if the user actually entered numbers
if largest_num is not None:
    print(f"Largest Number = {largest_num}")
    print(f"Smallest Number = {smallest_num}")
else:
    print("No numbers were entered.")
