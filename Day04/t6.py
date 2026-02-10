import time
class Bosch_ErrorBank(Exception):
  def __init__(self, Msg, UserName, TimeStamp):
    super().__init__( Msg, UserName, TimeStamp)
    #FILE HANDLING CODE HERE to save the error at my own log file
     
try:
  raise Bosch_ErrorBank("Some Internal Problem","Harmeet", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
  x = int(input("Enter a number: "))
  result = 10 / x
except ZeroDivisionError:
  print("Cannot divide by zero!")
except ValueError:
  print("Invalid input. Enter a number.")
except Bosch_ErrorBank as e:
  print(f"Own Issue {e}") 
finally:
  print("Thanks")

