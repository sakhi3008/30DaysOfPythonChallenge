# Challenge - Check if a user-entered number is prime

user_input = int(input("Enter your number: "))

if user_input < 2:
  print(f"{user_input} is not a prime number")
else:
  for i in range(2, user_input):
    if user_input % i == 0:
      print(f"{user_input} is not a prime number")
      break
  else:
    print(f"{user_input} is a prime number")
