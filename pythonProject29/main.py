import random as rnd

mistakes = 0

words = ['кот', 'ток',  'рог',  'сон', 'нос', 'рис',  'куб',
          'нож', ]
word = rnd.choice(words)

def dead_st1():
    print('\r')
    print('\r')
    print('     /|')

def dead_st2():
    print('\r')
    print('      |')
    print('      |')

def dead_st3():
    print('      |')
    print('      |')
    print('      |')
    print('      |')

def dead_st4():
    print('   ---|')
    print('      |')
    print('      |')
    print('      |')

def person_st1():
    print('  o---|')
    print('      |')
    print('      |')
    print('     /|')

def person_st2():
    print('  o---|')
    print('  |   |')
    print('      |')
    print('     /|')

def person_st3():
    print('  \o--|')
    print('   |  |')
    print('      |')
    print('     /|')

def person_st4():
    print('  \o/-|')
    print('   |  |')
    print('      |')
    print('     /|')

def person_st5():
    print('  \o/-|')
    print('   |  |')
    print('  /   |')
    print('     /|')


def person_st6():
    print('  \o/-|')
    print('   |  |')
    print('  / \ |')
    print('     /|')

while True:
    enter = input("Буква: ")

    if enter in word:
        print("Правильно!")
    else:
        mistakes += 1

        if mistakes == 1:
            dead_st1()
        elif mistakes == 2:
            dead_st2()
        elif mistakes == 3:
            dead_st3()
        elif mistakes == 4:
            dead_st4()
        elif mistakes == 5:
            person_st1()
        elif mistakes == 6:
            person_st2()
        elif mistakes == 7:
            person_st3()
        elif mistakes == 8:
            person_st4()
        elif mistakes == 9:
            person_st5()
        elif mistakes == 10:
            person_st6()
            break
