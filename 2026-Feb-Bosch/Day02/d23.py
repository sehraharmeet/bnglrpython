# Normal function definition
def add(x, y):
    x=x+10
    y=y+20
    return x + y

# Equivalent dlambda function
#add_lambda = lambda x, y: x + y
add = lambda x, y: (x + 10) + (y + 20)


# Using the lambda function
result = add_lambda(5, 3)
print(result)  # Output: 8


numbers = [1, 2, 3, 4]

result = list(map(lambda x: x + 10, numbers))
print(result)