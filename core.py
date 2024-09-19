#------------------setup----------------#
import random
def ask(Question):
    return input(Question +"\n>>> ")
# intro and outro text -------------------------#
intro = '''Who knows what this abandoned basement holds?
It's time to find out, one way or another.
Drawing your sword, you prepare for the challenges ahead
You climb down the stairs ready for adventure.'''
victory = '''With the last monster slain you tend to your wounds and sheath your sword.\n'''
outro1 = '''You have slain '''
outro2 = ''' monsters and looted '''
outro3 = ''' treasure chests.
Wounded and exhausted, you climb the stairs back to the surface.
You earned a total score of '''
outro4 = ''' points on your adventure.'''
defeat = '''Alas, the monsters were too much for you.
Forgetting about the rest of the treasure,
you head for the stairs back to the surface.'''
#----------------------------------------------------#


#-------------------Decision prompts-------------------#
Action = '''What do you want to do?
(attack, loot, flee)'''
choice0 = '''You have cleared this room.
Do you wish to proceed or retrace your steps?
(proceed, return)'''
choice1 ='''There is a door to your left and a door 
to your right. Which path do you want to take?
(left, right)'''
choice2 ='''There is a door to your left and a door
ahead of you. Which path do you want to take?
(left, forward)'''
go = 'You proceed through the door'
back = 'You return through the door you entered from'
combat = 'The monster notices you and attacks!'
#----------------------------------------------------#


#--------------------Variables-----------------------#
playerHealth = [100] # my sneaky way of bypassing the global vs local issue - it lets you edit a list but not change an int. So, I create a list and use element 0
playerStrength = 5
playerDefense = 6
monsterHealth = 20 
monsterStrength = 4
monsterDefense = 0
monstersSlain = [0]
chestsLooted = [0]
playerroom = [0]
wonGame = [False]
#damage = 2d8 + strength - 2d6 + defense 
#---------------------------------------------#



#--------------elements graphics--------------------#
monsterLine1 = ''' "\\ ^•_•^ /" '''
monsterLine2 = '''    (   )    '''
monsterLine3 = '''    ,/ \\,    '''
monsterWidth = '''             ''' #13

treasureLine1 = ''' (--(__  '''
treasureLine2 = ''' |_|===| '''
treasureWidth = '''         '''#9

doorLine1 = '''  ___  '''
doorLine2 = ''' |  _| '''
doorLine3 = ''' |   | '''
doorWidth = '''       '''#7

top = ''' __________________________________\n'''
wall = '|'
floor = ' ----------------------------------'
empty = wall + ' '*34 + wall +'\n' 
#-------------------------------------------#

#------------------map----------------------#
''' 
    [en1]     [ t5]
    [ m2][ m3][tm4]
              [ m6][tm7]
         [ex9][ t8]
''' 
#-------------------------------------------#

#-------------------Spacing-----------------#
gapM = ' '*((34-13)//2)
gapT=' '*((34-9)//2)
gapMT=' '*((34-22)//3)
gapD=' '*((34-7)//2)
gap2D = ' '*((34-14))
n = '\n'
#-------------------------------------------#

#----------------Larger elements--------------#
Monster = wall+ gapM +monsterLine1+gapM+' '+wall+n +wall+ gapM +monsterLine2+gapM+' '+wall+n +wall+ gapM +monsterLine3+gapM+' '+wall+n
Treasure = wall +gapT +treasureLine1+gapT+' '+wall+n +wall+gapT+treasureLine2+gapT+' '+wall+n
MonsterTreasure =wall+gapMT+monsterLine1+gapMT+treasureWidth+gapMT+wall+n  +wall+gapMT+monsterLine2+gapMT+treasureLine1+gapMT+wall+n +wall+gapMT+monsterLine3+gapMT+treasureLine2+gapMT+wall+n
Door = wall+gapD+doorLine1+gapD+' '+wall+n +wall+gapD+doorLine2+gapD+' '+wall+n +wall+gapD+doorLine3+gapD+' '+wall+n
leftDoor = wall+doorLine1+gapD*2+' '+wall+n+wall+doorLine2+gapD*2+' '+wall+n+wall+doorLine3+gapD*2+' '+wall+n
rightDoor = wall+' '+gapD*2+doorLine1+wall+n+wall+' '+gapD*2+doorLine2+wall+n+wall+gapD*2+' '+doorLine3+wall+n
sideDoors = wall+doorLine1+gap2D+doorLine1+wall+n+wall+doorLine2+gap2D+doorLine2+wall+n+wall+doorLine3+gap2D+doorLine3+wall+n
#---------------------------------------------#

#-----------------------rooms-----------------#
room0= top+empty*9+Door+floor
room1 = top+Door+empty*3+Monster+empty*3+floor 
r1c = top+Door+empty*9+floor
room2 = top+Door+empty*3+Monster+empty*3+floor 
r2c = top+Door+empty*9+floor
room3 = top+empty*3+MonsterTreasure+ sideDoors+floor
r3m = top + empty*3+Monster+empty*5+floor
r3t = top+empty*4+Treasure+sideDoors+floor
r3c = top+empty*9+sideDoors+floor
room4 = top+empty*7+Treasure+empty*3+floor
r4c = top+empty*12+floor
room5 = top+Door+empty*2+Monster+leftDoor+empty+floor
r5c = top+Door+empty*5+leftDoor+empty+floor
room6 = top+empty*4+MonsterTreasure+empty*5 
r6m = top + empty*4+Monster+empty*5+floor
r6t = top+empty*5+Treasure+empty*5+floor
r6c = top+empty*12+floor
room7 = top+empty*3+Treasure+empty+rightDoor+empty*3+floor
r7c = top + empty*6+rightDoor+empty*3+floor
room8 = top+empty*9+Door+floor
rooms = [room0,room1,room2,room3,room4,room5,room6,room7,room8]
emptyRooms = [room0,r1c,r2c,r3c,r4c,r5c,r6c,r7c,room8]
roomsWithMonsters = [False,True,True,True,False,True,True,False,False]
monstersHealth = [20,20,20,20,20,20,20,20,20]
roomsWithChests = [False,False,False,True,True,False,True,True,False]
#--------------------------------------------#

#-------------descriptions-------------------#
tmDesc ='''There is a monster in the center of the room guarding a treasure chest.''' 
mDesc = '''There is a monster in the center of the room.'''
tDesc = '''There is a treasure chest in the center of the room.'''
emDesc = '''The room is empty except for the doors.'''
enDesc = '''The room is empty except for the stairs and door'''
#---------------------------------------------------#


#------------------Function Setup-------------------#
def checkRoom(r):
        if roomsWithChests[r]:
            return True
        else:
            return False
def checkMonster(r):
        if roomsWithMonsters[r]:
            return True
        else:
            return False
def drawRoom(r):
    print(rooms[r])
    print(r)
    print(playerroom[0])
def battle(room):
    drawRoom(room)
    act = ask(Action)
    if act == 'attack':
        damage = random.randint(1,8) + random.randint(1,8) + playerStrength - random.randint(1,6) - random.randint(1,6)
        monstersHealth[room] = monstersHealth[room]-damage
        print('You attack the monster for '+str(damage)+' damage!')
        print('The monster has '+str(monstersHealth[room])+' health remaining.')
        if monstersHealth[playerroom[0]] > 0:
            damage = random.randint(1,8) + random.randint(1,8) + monsterStrength - random.randint(1,6) - random.randint(1,6) - 6
            playerHealth[0] = playerHealth[0] - damage
            print('The monster attacks you for '+str(damage)+' damage!')
            print('You have '+str(playerHealth)+' health remaining.')
            battle(playerroom[0])
        elif monstersHealth[playerroom[0]] <= 0 :
            print("You slay the monster")
            monstersSlain[0] = monstersSlain[0] + 1
            roomsWithMonsters[room] = False
            if checkRoom(room):        
                print('With the monster defeated, you safely loot the treasure chest.')
                chestsLooted[0] = chestsLooted[0] + 1
                roomsWithChests[room] = False
            rooms[room] = emptyRooms[room]
            
    elif act == 'loot':
        if checkRoom(room):
            chestsLooted[0] = chestsLooted[0] + 1
            roomsWithChests[room] = False
            if room == 3:
                rooms[room] = r3m
            elif room == 4:
                rooms[room] = r4c
            elif room == 6:
                rooms[room] = r6m
            elif room == 7:
                rooms[room] = r7c
            print('You loot the treasure chest. \nWhile you do, the monster siezes the opportunity and attacks!')
            damage = random.randint(1,8) + random.randint(1,8) + monsterStrength - random.randint(1,6) - random.randint(1,6) - 6
            playerHealth[0] = playerHealth[0] - damage
            print('The monster attacks you for '+str(damage)+' damage!')
            print('You have '+str(playerHealth[0])+' health remaining.')
            battle(room)
        else:
            print('there is nothing to loot in here!')
            battle(room)
    elif act == 'flee':
        print(defeat)
    elif act == 'exit':
            potato == 'amazing'
    elif act == 'quit':
            potato = 'amazing'
    else:
        print('Please enter a valid response')
        battle(room)
    
def printDesc(room):
    if checkMonster(room):
        if checkRoom(room):
            print(tmDesc)
        else:
            print(mDesc)
    elif checkRoom(room):
        print(tDesc)
    elif room == 0 or room ==8:
        print(enDesc)
    else:
        print(emDesc)
def choosePath(room):
    if room ==4:
        path = ask(choice1)
        if path == 'left':
            playerroom[0] = 5
            room = playerroom[0]
        elif path == 'right':
            playerroom[0] = 6
            room = playerroom[0]
        else:
            print('please enter a valid response')
            choosePath(playerroom[0])
    elif room ==6:
        path = ask(choice2)
        if path == 'forward':
            playerroom[0] = 8
            room = playerroom[0]
        elif path == 'left':
            playerroom[0] = 7
            room = playerroom[0]
        elif path == 'exit':
            potato == 'amazing'
        elif path == 'quit':
            potato = 'amazing'
        else:
            print('please enter a valid response')
            choosePath(playerroom[0])

def travel(room):
    drawRoom(room)
    if checkMonster(playerroom[0]):
        battle(playerroom[0])
    elif checkRoom(playerroom[0]):
        drawRoom(playerroom[0])
        print('You loot the treasure chest')
        chestsLooted[0] = chestsLooted[0]+1
        for i in range(4):
                if roomsWithChests[i] == playerroom[0]:
                    roomsWithChests[i] = 9
        rooms[playerroom[0]] = emptyRooms[playerroom[0]]
    way = ask(choice0)
    if way == 'proceed':
        if room == 4 or room ==6:
            choosePath(room)
            room = playerroom[0]
        elif room == 8:
            wonGame[0] = [True]
            print(victory)

        else:
            playerroom[0] = room +1
            room = playerroom[0]
    elif way == 'return':
        if room == 6:
            playerroom[0] = 4
            room = playerroom[0]
        else:
            playerroom[0] = room-1
            room = playerroom[0]
    elif way == 'exit':
            potato == 'amazing'
    elif way == 'quit':
            potato = 'amazing'
    else:
        print('please enter a valid response')
        travel(playerroom[0])
    printDesc(playerroom[0])
    
    if not wonGame[0]:
        travel(playerroom[0])

 #-------------Begin Executing--------------------#       
playerName = ask('''What's your name?''')
print("hello, "+playerName+'.')
print('Welcome to the game.')
print(intro)
travel(playerroom[0])
print(outro1 + str(monstersSlain[0]) + outro2 + str(chestsLooted[0]))
print(outro3+str(200*monstersSlain[0]+100*chestsLooted[0])+outro4)
