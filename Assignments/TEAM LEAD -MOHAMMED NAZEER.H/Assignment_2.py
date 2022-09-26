import random
def high(t):
    if t>45:
        print("alarm-on")
    else:
        print("alarm-off")

while(1):
    temperature=random.randint(25,100)
    humidity=random.randint(0,100)
    print(temperature)
    print(humidity)
    high(temperature)
print("\n")
