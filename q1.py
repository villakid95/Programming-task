import random

def shuffle (mixer):
    newList = []

    while len (mixer)!=0:
        randomPosition = random.randint (0,len(mixer)-1)

        randomNumber = mixer.pop (randomPosition)
        newList.append (randomNumber)

    return newList

originalList = list(range(1,10))

print("Original List: {}".format(originalList))

completedList = shuffle(originalList)
print("Shuffled List: {}".format(completedList))
      
#In this code when there is elements in mixer then it creates a random number the size of the length of the arrray. A new list is made as each number is added into the list in a new random assigned position
#Run time bounds of the function above are 0(n)
