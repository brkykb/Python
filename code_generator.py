import random
print("You can generate code if you write \"generate\"")
c = input()
if c == ("generate"):
    x = random.randrange(10)
    y = random.randrange(10)
    z = random.randrange(10)
    a = random.randrange(10)
    b = random.randrange(10)
    d = random.randrange(10)
    print(x, y, z, a, b, d)
else:
    print("Try again!")

