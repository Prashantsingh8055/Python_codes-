numbers = (10, 20, 30, 40, 50, 60)

search = int(input("Enter number to search: "))

found = False

for num in numbers:
    if num == search:
        found = True
        break

if found:
    print("Number is present in tuple")
else:
    print("Number not present in tuple")