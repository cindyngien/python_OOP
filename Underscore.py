#1
def my_filter(lst, func):
    output = []
    for item in lst:
        if func(item):
            output.append(item)

    return output

print my_filter([1,2,3,4,5], lambda x: x%2==0)

#2
def my_reject(lst, func):
    output = []
    for item in lst:
        if not func(item):
            output.append(item)

    return output

print my_reject([1,2,3,4,5], lambda x: x%2==0)

#3
def my_find(lst, func):
    for item in lst:
        if func(item):
            return item

    return None
print my_find([1,2,3,4,5], lambda x: x%2==0)

#4
def my_all(lst, func):
    for item in lst:
        if not func(item):
            return False
    return True
print my_all([1,2,3,4,5], lambda x: x%2==0)

#5
def my_any(lst, func):
    for item in lst:
        if func(item):
            return True
    return False
print my_any([1,2,3,4,5], lambda x: x%2==0)
