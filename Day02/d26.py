accept_numbers = lambda: [float(input(f"Enter number {i+1}: ")) for i in range(10)]
display_numbers = lambda nums: print("\nNumbers you entered:\n" + "\n", nums)
display_max_number = lambda nums: print(f"\nThe maximum number is: {max(nums)}")

numbers = accept_numbers()
display_numbers(numbers)
display_max_number(numbers)