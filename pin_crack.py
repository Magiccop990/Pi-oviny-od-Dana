import random, time

pin = 1234
nl = []

print("Cracking pin has now begun...")
time.sleep(1)

def RandNum():
    global pin_guess
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    num = str(num1) + str(num2) + str(num3) + str(num4)
    pin_guess = int(num)
    if pin_guess in nl:
        RandNum()

while True:
    global num, pin_guess
    RandNum()
    nl.append(pin_guess)
    print(f"\rGuessing pin: {pin_guess}...", end="")
    time.sleep(0.005)
    if pin == pin_guess:
        print(f"\nCrack succsess... The pin was: {pin_guess}")
        break
