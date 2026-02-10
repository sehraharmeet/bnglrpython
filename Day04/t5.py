# try:
#     x=10/0
#     print("thanks")
# except:
#     print("some issue")

try:  
  raise Exception
  x = int(input("Enter a number: "))
  result = 10 / x  
except ZeroDivisionError as z:
  print(f"Cannot divide by zero!{z}")
except ValueError as z:
  print("Invalid input. Enter a number.")
except Exception as e:
  print(f"Other Error.{e}")
else:
    print("ok")

# try: 
#  raise Exception
#  x = int(input("Enter a number: ")) #2
#  result = 10 / x
# except ZeroDivisionError as e:
#  print(f"Cannot divide by zero! ==> {e}")
# except ValueError as e:
#  print(f"Invalid input. Enter a number. ==> {e}")
# except Exception as e:
#   print(f"YESSS ==> {e}")
# else:
#   print("All good")
# finally:
#   print("SUPERRRRR")

