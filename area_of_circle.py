def area(r):
    return (22/7) * r * r 

radius = float(input("Type your radius: "))
result = area(radius)
print(f"The area of the circle is {result}")


def bigger_number(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Number 1: "))
b = int(input("Number 2: "))


print("The bigger number is:", bigger_number(a, b))
