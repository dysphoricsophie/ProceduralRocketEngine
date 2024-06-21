import random, string, sys
guess, count, user_pass = "", 0, "1ty?"
while guess != user_pass:
    guess = ""
    for a in range(8):
        guess = str(random.choice(string.ascii_letters)) + guess
    sys.stdout.write("\rNumber of attempts: " + str(count))
    sys.stdout.flush()
    count = count+1
print(f"\n\nYour key is {guess}\nNumber of attempts: {format(int(count), ',')}")