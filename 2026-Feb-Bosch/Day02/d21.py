numbers = ["1", "2", "3", "4"]
int_numbers = list(map(int, numbers))
print(int_numbers) 

names = ["harmeet", "aman", "riya", "karan"]
#first way
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)
#second way
upper_names = [name.upper() for name in names]
print(upper_names)
#third way
new_names=list(map(str.upper,names))
print(new_names)
