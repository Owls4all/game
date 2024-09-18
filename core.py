#------------------setup----------------#
import random
def ask(Question):
    return input(Question +"\n>>> ")
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


Action = '''What do you want to do?
(attack, defend, loot, flee)'''
defeat = '''Alas, the monsters were too much for you.
Forgetting about the rest of the treasure,
you head for the stairs back to the surface.'''


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



playerHealth = 100
playerStrength = 5
playerDefense = 6
monsterHealth = 20 
monsterStrength = 4
monsterDefense = 0
monstersSlain = 0
chestsLooted = 0
room = 1
roomsCleared = 0
#damage = 2d8 + strength - 2d6 + defense 
#--------------more setup--------------------#
monsterLine1 = ''' "\ ^•_•^ /" '''
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

''' 
    [en1]     [ t5]
    [ m2][ m3][tm4]
              [ m6][tm7]
         [ex9][ t8]
''' 

gapM = ' '*((34-13)//2)
gapT=' '*((34-9)//2)
gapMT=' '*((34-22)//3)
gapD=' '*((34-7)//2)
gap2D = ' '*((34-14))
n = '\n'
Monster = wall+ gapM +monsterLine1+gapM+' '+wall+n +wall+ gapM +monsterLine2+gapM+' '+wall+n +wall+ gapM +monsterLine3+gapM+' '+wall+n
Treasure = wall +gapT +treasureLine1+gapT+' '+wall+n +wall+gapT+treasureLine2+gapT+' '+wall+n
MonsterTreasure =wall+gapMT+monsterLine1+gapMT+treasureWidth+gapMT+wall+n  +wall+gapMT+monsterLine2+gapMT+treasureLine1+gapMT+wall+n +wall+gapMT+monsterLine3+gapMT+treasureLine2+gapMT+wall+n
Door = wall+gapD+doorLine1+gapD+' '+wall+n +wall+gapD+doorLine2+gapD+' '+wall+n +wall+gapD+doorLine3+gapD+' '+wall+n
leftDoor = wall+doorLine1+gapD*2+' '+wall+n+wall+doorLine2+gapD*2+' '+wall+n+wall+doorLine3+gapD*2+' '+wall+n
rightDoor = wall+' '+gapD*2+doorLine1+wall+n+wall+' '+gapD*2+doorLine2+wall+n+wall+gapD*2+' '+doorLine3+wall+n
sideDoors = wall+doorLine1+gap2D+doorLine1+wall+n+wall+doorLine2+gap2D+doorLine2+wall+n+wall+doorLine3+gap2D+doorLine3+wall+n

room0= top+empty+9+Door+floor
room1 = top+Door+empty*3+Monster+empty*3+floor 
room2 = top+Door+empty*3+Monster+empty*3+floor 
room3 = top+empty*3+MonsterTreasure+ sideDoors + floor
room4 = top+empty*7+Treasure+empty+3+floor
room5 = top+Door+empty*2+Monster+leftDoor+empty+floor
room6 = top+empty*4+MonsterTreasure+empty*5 
r6m = top + empty*4+Monster+empty*5+floor
r6t = top+empty*5+Treasure+empty*5+floor
r6c = top+empty*12+floor
room7 = top+empty*3+Treasure+empty+rightDoor+empty*3+floor
r7c = top + empty*6+rightDoor+empty*3+floor
room8 = top+empty*9+Door+floor
rooms = [room0,room1,room2,room3,room4,room5,room6,room7,room8]
roomsWithMonsters = [1,2,3,5,6]
roomsWithChests = [3,4,6,7]
tmDesc ='''There is a monster in the center of the room guarding a treasure chest.''' 
mDesc = '''There is a monster in the center of the room.'''
tDesc = '''There is a treasure chest in the center of the room.'''
emDesc = '''The room is empty except for the doors.'''
enDesc = '''The room is empty except for the stairs and door'''
#---------------------------------------------------#

#------------------Function Setup-------------------#
def drawRoom(r):
    print(r)
def battle(room):
    act = ask(Action)
    if act == 'attack':
        damage = random.randint(1,8) + random.randint(1,8) + playerStrength - random.randint(1,6) - random.randint(1,6)
        monsterHealth = monsterHealth - damage
        if monsterHealth > 0:
            damage = random.randint(1,8) + random.randint(1,8) + playerStrength - random.randint(1,6) - random.randint(1,6) - 6
            playerHealth = playerHealth - damage
        else:
            print("You slay the monster")
            monstersSlain = monstersSlain + 1
    elif act == 'loot':
        b = 'f'
    elif act == 'flee':
        print(defeat)
        print(outro1 + monstersSlain + outro2 + chestsLooted)

    
