# recreating the vibe of coc like games
points = 0




def main():
    print('main menu')



def rock_paper_scissor():
    x = input('Enter your choice(r/p/s): ')
    def user():
        global a
        if x == 'r' or x == 'R':
            a = 'rock'
        elif x == 'p' or x == 'P':
            a = 'paper'
        elif x == 's' or x == 'S':
            a = 'scissor'
        else:
            rock_paper_scissor()
    def PC():
        global b
        import random
        c = random.randrange(1,9)
        if c <=3:
            b = 'rock'
        elif 4<=c<=6:
            b = 'paper'
        elif 7<=c<=9:
            b = 'scissor'
        else:
            print('Sorry... An error occured! pls try again')
            rock_paper_scissor()
    def result():
        global points
        if a == 'rock' and b == 'rock':
            points = points -1
            print('you choose rock')
            print('computer also chooses rock')
            print('you lost')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                rock_paper_scissor()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()
        elif a == 'paper' and b == 'paper':
            points = points -1
            print('you choose paper')
            print('computer also chooses paper')
            print('you lost')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                rock_paper_scissor()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()
        elif a == 'scissor' and b == 'scissor':
            points = points -1
            print('you choose scissor')
            print('computer also chooses scissor')
            print('you lost')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                rock_paper_scissor()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()
        elif a == 'rock' and b == 'paper':
            points+=5
            print('you choose rock')
            print('computer chooses paper')
            print('you won')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                rock_paper_scissor()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()
        elif a == 'rock' and b == 'scissor':
            points+=5
            print('you choose rock')
            print('computer chooses scissor')
            print('you won')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                rock_paper_scissor()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()
        elif a == 'paper' and b == 'rock':
            points+=5
            print('you choose paper')
            print('computer chooses rock')
            print('you won')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                rock_paper_scissor()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()
        elif a == 'paper' and b == 'scissor':
            points+=5
            print('you choose paper')
            print('computer chooses scissor')
            print('you won')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                rock_paper_scissor()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()
        elif a == 'scissor' and b == 'rock':
            points+=5
            print('you choose scissor')
            print('computer chooses rock')
            print('you won')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                rock_paper_scissor()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()
        elif a == 'scissor' and b == 'paper':
            points+=5
            print('you choose scissor')
            print('computer chooses paper')
            print('you won')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                rock_paper_scissor()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()
        else:
            rock_paper_scissor()
    user()
    PC()
    result()




def odd_eve():
    x = input('Enter your choice(o/e): ')
    def user():
        global a
        if x == 'o' or x == 'O':
            a = 'odd'
        elif x == 'e' or x == 'E':
            a = 'even'
        else:
            odd_eve()
    def PC():
        global d
        import random
        c = random.randrange(0,100)
        if c%2 == 0:
            d = 'odd'
        elif c%3 != 0:
            d = 'even'
        else:
            print('Sorry... An error occured! pls try again')
            odd_eve()
    def result():
        global points
        if a == 'odd' and d == 'odd':
            points += 1
            print('you choose odd')
            print('computer also chooses odd')
            print('you won')
            print('your points are: ',points)
            y = input('what will you choose(bat/bowl): ')
            if y == 'bat':
                batting()
            elif y == 'bowl':
                bowling()
            else:
                odd_eve()
        elif a == 'even' and d == 'even':
            points += 1
            print('you chooses even')
            print('computer also chooses even')
            print('you won')
            print('your points are: ',points)
            y = input('what will you choose(bat/bowl): ')
            if y == 'bat':
                batting()
            elif y == 'bowl':
                bowling()
            else:
                odd_eve()
        elif a == 'odd' and d == 'even':
            points = points
            print('you choose odd')
            print('computer chooses even!')
            print('you lost')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                odd_eve()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()
        elif a == 'even' and d == 'odd':
            points = points
            print('you chooses even')
            print('computer chooses odd')
            print('you lost')
            print('your points are: ',points)
            z = input('Do you want to play more(y/n): ')
            if z == 'y' or z == 'Y':
                odd_eve()
            elif z == 'n' or z == 'N':
                main()
            else:
                main()

    def batting():
        global points
        x = input('choose what run to score(1-6): ')
        q = [1,2,3,4,5,6]
        score = 0
        cscore = 0
        if x in q:
            import random
            g = random.choose(q)
            if x != g:
                score+=x
                print('your score is: ',score)
                batting()
            else:
                print('you are out')
                print('your total score are: ',score)
                print('Now it is your turn to bowl')
                def bol():
                    global points
                    global score
                    global cscore
                    global q
                    y = input('choose what to bowl(1-6): ')
                    if y in q:
                        f = random.choose(q)
                        if y != f:
                            cscore+=y
                            if cscore > score:
                                print('you lost')
                                points = points -2
                                print('your points are: ',points)
                            else:
                                bol()
                        else:
                            print('computer out')
                            print('you win')
                            s = score - cscore
                            points = points + s
                            print('your points are: ',points)
                    else:
                        bol()
                bol()
                            
        else:
            batting()
    def bowling():
        global points
        x = input('choose what to bowl(1-6): ')
        q = [1,2,3,4,5,6]
        score = 0
        cscore = 0
        if x in q:
            import random
            g = random.choose(q)
            if x != g:
                cscore+=x
                print('computer score is: ',cscore)
                bowling()
            else:
                print('computer out')
                print('computer total score is are', cscore)
                print('Now it is your turn to bat')
                def bat():
                    global points
                    global score
                    global cscore
                    global q
                    y = input('choose what run to score(1-6): ')
                    if y in q:
                        f = random.choose(q)
                        if f != y:
                            score+=y
                            if score > cscore:
                                print('you won')
                                points = points + 10
                                print('your points are: ',points)
                            else:
                                bat()
                        else:
                            print('You are out')
                            print('you lost')
                            s = cscore - score
                            points = points -s
                            print('your points are: ',points)
                    else:
                        bol()
                bol()
        else:
            bowling()

            
    user()
    PC()
    result()

def quiz():
    global points
    print('In this you have to answer 5 computer science questions')
    def first():
        global a
        print('question 1:' '\n'
              'who is regarded as the father of Computers?' '\n'
              'option 1: Charles Babbage' '\n'
              'option 2: Alan Turing' '\n'
              'option 3: Linus Torvalds' '\n'
              'option 4: Ada Lovelace' '\n')
        x = input('Enter your answer(1/2/3/4): ')
        if x == '1':
            print('correct answer')
            a = 1
        else:
            a=0
            print('your answer was wrong')
    def second():
        global b
        print('question 2:' '\n'
              'What is the full form of OS?' '\n'
              'option 1: order of significance' '\n'
              'option 2: open software' '\n'
              'option 3: operationg system' '\n'
              'option 4: optical sensor' '\n')
        x = input('Enter your answer(1/2/3/4/5): ')
        if x == '3':
            b = 1
        else:
            b=0
            print('your answer was wrong')
    def third():
        global c
        print('question 3:' '\n'
              'what is the full form of PDF?' '\n'
              'option 1: portable document format' '\n'
              'option 2: prntable document format' '\n'
              'option 3: public document format' '\n'
              'option 4: published document format' '\n')
        x = input('Enter your answer(1/2/3/4): ')
        if x == '1':
            print('correct answer')
            c = 1
        else:
            c=0
            print('your answer was wrong')
    def fourth():
        global d
        print('question 4:' '\n'
              'What is the full form of CPU?' '\n'
              'option 1: Computer Processing Unit' '\n'
              'option 2: Computer Principle Unit' '\n'
              'option 3: Central Processing Unit' '\n'
              'option 4: Control Processing Unit' '\n')
        x = input('Enter your answer(1/2/3/4): ')
        if x == '3':
            print('corect answer')
            d = 1
        else:
            d=0
            print('your answer was wrong')
    def fifth():
        global e
        print('question 5:' '\n'
              'Which of the following language does the computer understand?' '\n'
              'option 1: C Language' '\n'
              'option 2: Assembly Language' '\n'
              'option 3: Binary Language' '\n'
              'option 4: BASIC' '\n')
        x = input('Enter yur answer(1/2/3/4): ')
        if x == '3':
            print('correct answer')
            e = 1
        else:
            e=0
            print('your answer was wrong')
    def result():
        global points
        global a
        global b
        global c
        global d
        global e
        first()
        second()
        third()
        fourth()
        fifth()
        result = a+b+c+d+e
        print('your score was: ',result)
        points = points + result
        print('your points are: ',points)
    result()
odd_eve()
