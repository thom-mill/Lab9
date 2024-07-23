def encode(nums):
  new_string = ''
  for num in nums:
    new_string += (int(num) + 3)%10
  return new_string



while True:
    print("Menu")
    print("-----")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    option = int(input("Please enter an option: "))
    if option == 1:
      password = input("Enter password to be encoded: ")
      print("Your encoded password is", encode(password))
    elif option == 2:
      print("Return decoded password")
    elif option == 3:
      break
    else:
      print("Invalid option")