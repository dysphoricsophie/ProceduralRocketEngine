import sys
import random
from time import time

def data():
    weaponry = ["Knife", "Sword", "Shield", "Tranquilizer Gun", "None",
                "Full Armor", "Enchanted Amulet", "PickAxe", "Shovel",  "Hammer", "Baseball Bat", "Submachine Gun",
                "Wrench", "Metal Pole", "Taser"]
    random.shuffle(weaponry)
    age = random.randint(16, 100)
    strength = random.randint(2, 25)
    speed = random.randint(2, 25)
    intel = random.randint(2, 25)
    height = random.randint(100, 250)
    weapon = str(f"{random.choice(weaponry)}")
    return [age, strength, speed, intel, height, weapon]
def ass(People):
    while len(People) != 2:
        ChoiceA, ChoiceB, ChoiceC, ChoiceD = random.choice(People), random.choice(People), random.choice(People), random.choice(People)
        chosen, scores = [ChoiceA, ChoiceB, ChoiceC, ChoiceD], [0, 0, 0, 0]
        for i in range(1, 5):
            if i == 1:
                if ChoiceA[i] < ChoiceB[i] or ChoiceA[i] < ChoiceC[i] or ChoiceA[i] < ChoiceD[i]: scores[0] = scores[0] + i
                if ChoiceB[i] < ChoiceA[i] or ChoiceB[i] < ChoiceC[i] or ChoiceB[i] < ChoiceD[i]: scores[1] = scores[1] + i
                if ChoiceC[i] < ChoiceA[i] or ChoiceC[i] < ChoiceB[i] or ChoiceC[i] < ChoiceD[i]: scores[1] = scores[2] + i
                if ChoiceD[i] < ChoiceA[i] or ChoiceD[i] < ChoiceB[i] or ChoiceD[i] < ChoiceC[i]: scores[1] = scores[3] + i
            else:
                if ChoiceA[i] > ChoiceB[i] or ChoiceA[i] > ChoiceC[i] or ChoiceA[i] > ChoiceD[i]: scores[0] = scores[0] + i
                if ChoiceB[i] > ChoiceA[i] or ChoiceB[i] > ChoiceC[i] or ChoiceB[i] > ChoiceD[i]: scores[1] = scores[1] + i
                if ChoiceC[i] > ChoiceA[i] or ChoiceC[i] > ChoiceB[i] or ChoiceC[i] > ChoiceD[i]: scores[1] = scores[2] + i
                if ChoiceD[i] > ChoiceA[i] or ChoiceD[i] > ChoiceB[i] or ChoiceD[i] > ChoiceC[i]: scores[1] = scores[3] + i
        for i in scores:
            if i == min(scores):
                print(f"\n{chosen}")
                print(scores)
                print(chosen[scores.index(i)])
                print(People[int(chosen[scores.index(i)][0].split(": ")[1])-1])
                People.remove(chosen[scores.index(i)])
        sys.stdout.write(f"\rPeople Left: {format(int(len(People)), ',')}")
        sys.stdout.flush()
class App:
    def __init__(self):
        start = time()
        Peoples = []
        for i in range(1, (120000+1)):
            person = data()
            person.insert(0, str(f"Id: {i}"))
            Peoples.append(person)
            sys.stdout.write(f"\rPeople Populated: {format(int(i), ',')}")
            sys.stdout.flush()
        ass(Peoples)
        print(f"\nTime Taken: {str(time() - start)} seconds")
        Edata = ["Age", "Strength", "Speed", "Intelligence", "Height", "Weaponry"]
        for x in Peoples:
            for y in x:
                if x.index(y) == 0:
                    print(f"\n{y}")
                else:
                    print(f"{Edata[x.index(y)-1]}: {y}")

if __name__ == "__main__":
    app = App()
