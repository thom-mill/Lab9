def encode(password):
    enc = ''
    for i in range(len(password)):
        enc += str(int(password[i])+3)
    return enc

def decode(nums):
  dec = ''
  for i in range(len(password)):
      dec += str(int(password[i])-3)
  return dec

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
      print(f"Your encoded password is {encode(password)}\n")
    elif option == 2:
      print("Return decoded password")
    elif option == 3:
      print(f"The encoded password is {encode(password)}, and the original password is {decode(password)}.")
    else:
      print("Invalid option")