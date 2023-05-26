print("Hello! You are in the amusement park")
tall = float(input("What is you height in cm? "))
bill = 0

if tall >=120 :
  print("You can ride the game! :D")
  age = int(input("How old are you? "))
  if age <12 :
    bill = 10
    print("Child tickets are $10")
  elif age <=18 :
    bill = 15
    print("Youth tickets are $15")
  else:
    bill = 20
    print("Adult tickets are $20")
  
  photo = str(input("Do you want to photo? Yes or No. "))
  photo_total = bill+3
  if photo == "Yes":
    print(f"Okay, the total is ${photo_total}")
  else:
    print(f"Okay, you have to pay ${bill}")
else:
  print("You can't ride the game! :(")
