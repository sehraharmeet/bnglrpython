weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# 1
# for day in weekdays:
#     print(day)

# 2
iterator = iter(weekdays)
print(next(iterator))
print(next(iterator))

# 3
# class WeekDays:
#     def __init__(self, days):
#         self.days = days
#         self.index = len(days)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
        
#         self.index -= 1
#         return "Bosch" + self.days[self.index]


# wd = WeekDays(weekdays)

# for day in wd:
#     print(day)
