print('Welcome to Treasure Island! Your mission is to find the Hidden Treasure!')
direction = str(input('You come to a fork in the road, do you go left or right?\n> '))

if direction == 'left':
    cross = str(input('The road leads you to a lake. You see an island in the distance.  Do you swim to the island or wait for a boat?\n> '))

    if cross == 'wait':
        door = str(input('The boat arives and you make it across the frigid waters to the island. You stumble upon a cabin with three doors. Do you open the Red, Yellow or Blue door?\n> '))

        if door == 'yellow':
            print('You open the yellow door. It\'s very bright and takes your eyes a few moments to adjust to the light.  You see piles of gold, gems and treasures.  You signal to the boat captain, who helps you load the treasure and you head home.')
            print('\a\nCongrats, you have found the hidden treasure!')
        elif door == 'red':
            print('You open the red door and a ball of fire engulfs you. RIP.')
            print('\a\nGame Over!')
        elif door == 'blue':
            print('You open the blue door. It\'s dark and cold. You move forward into the darkness, but slip into some water and fall down a deep well. You\'re unable to get out of the well.')
            print('\a\nGame Over!')
        else:
            print('As you contemplate which door to choose, a grizzly bear emerges from the woods and eats your face. RIP!')
            print('\a\nGame Over!')
    else:
        print('You dive into the frigid waters and begin swimming for what seems like hours. The island still seems so distant. You\'re exhausted, cold and alone. Everything begins to get dark as you decend into the abyss below.')
        print('\a\nGame Over!')
else:
    print('After wandering for hours in the woods, the sun goes down and the noises start.. You\'re cold, scared and alone. You build a fire, but then they come..')
    print('\a\nGame Over!')