def add_all(*args):
    print(args)
    return sum(args)

print(add_all(1, 2)) 
print(add_all(1, 2, 3, 4)) 
print(add_all(*[4, 5, 6]))

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#show_info(name="Harmeet", age=25, city="Delhi")
dict1 = {"name": "Harmeet"}
dict2 = {"age": 25, "city": "Delhi"}

show_info(**dict1, **dict2)
