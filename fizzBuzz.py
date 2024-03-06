def fizz_buzz():
    result = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result += "FizzBuzz\n"
        elif i % 3 == 0:
            result += "Fizz\n"
        elif i % 5 == 0:
            result += "Buzz\n"
        else:
            result += str(i) + "\n"
    return result

output = fizz_buzz()
print(output)
