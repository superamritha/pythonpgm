a = int(input("Enter the number you want to reverse: "))
reverse_number = 0

while a > 0:
    digit = a % 10
    print(digit)
    reverse_number = reverse_number * 10 + digit
    print("rsfx",reverse_number)

    a = a // 10
    print("fsvfx",a)

print("Reverse is:", reverse_number)
