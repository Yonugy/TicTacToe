import numpy as np
import random
cor=np.array([[0,0,0],[0,0,0],[0,0,0]])
player_action=[]
situation=False
def showcase():
    for i in range(9):
        if i%3==0:
            print('|',end='')
        if cor[i//3,i%3]==0:
            print(' ',end='|')
        #Player mark
        elif cor[i//3,i%3]==1:
            print('x',end='|')
        #Computer mark
        else:
            print('O',end='|')
        if i%3==2:
            print()

def marking(stage):
    while True:
        sign=0
        if stage==0:
            mark=input('Please select the place you want to mark: ')
            sign=1
        elif stage==1:
            mark=input('%s, please select the place you want to mark:'%name1)
            sign=1
        elif stage==2:
            mark=input('%s, please select the place you want to mark:'%name2)
            sign=2
        if mark=='a1' and cor[0,0]==0:
            cor[0,0]=sign
            break
        elif mark=='a2' and cor[0,1]==0:
            cor[0,1]=sign
            break
        elif mark=='a3' and cor[0,2]==0:
            cor[0,2]=sign
            break
        elif mark=='b1' and cor[1,0]==0:
            cor[1,0]=sign
            break
        elif mark=='b2' and cor[1,1]==0:
            cor[1,1]=sign
            break
        elif mark=='b3' and cor[1,2]==0:
            cor[1,2]=sign
            break
        elif mark=='c1' and cor[2,0]==0:
            cor[2,0]=sign
            break
        elif mark=='c2' and cor[2,1]==0:
            cor[2,1]=sign
            break
        elif mark=='c3' and cor[2,2]==0:
            cor[2,2]=sign
            break
        else:
            if len(mark)==2:
                if mark[0] in 'abc' and mark[1] in '123':
                    print('This place is already marked. Please choose somewhere else.')
                else:
                    print('Please choose place by typing a1, a2, a3, b1, b2, b3, c1, c2 or c3.')
            else:
                print('Please choose place by typing a1, a2, a3, b1, b2, b3, c1, c2 or c3.')
    player_action.append(mark)

def compStart():
    if player_action[-1]!='b2':
        cor[1,1]=2
        return 'b2'
    else:
        global choose
        choose=random.randint(1,4)
        if choose==1:
            cor[0,0]=2
            return 'a1'
        elif choose==2:
            cor[0,2]=2
            return 'a3'
        elif choose==3:
            cor[2,0]=2
            return 'c1'
        else:
            cor[2,2]=2
            return 'c3'

def comp():
    #Computer took the middle
    #If can win just win
    if cor[1,1]==2:
        #|O| | |
        #| |O| |
        #| | |?|
        if cor[0,0]==2 and cor[2,2]==0:
            cor[2,2]=2
            return 'c3'
        #| |O| |
        #| |O| |
        #| |?| |
        elif cor[0,1]==2 and cor[2,1]==0:
            cor[2,1]=2
            return 'c2'
        #| | |O|
        #| |O| |
        #|?| | |
        elif cor[0,2]==2 and cor[2,0]==0:
            cor[2,0]=2
            return 'c1'
        #| | | |
        #|?|O|O|
        #| | | |
        elif cor[1,2]==2 and cor[1,0]==0:
            cor[1,0]=2
            return 'b1'
        #|?| | |
        #| |O| |
        #| | |O|
        elif cor[2,2]==2 and cor[0,0]==0:
            cor[0,0]=2
            return 'a1'
        #| |?| |
        #| |O| |
        #| |O| |
        elif cor[2,1]==2 and cor[0,1]==0:
            cor[0,1]=2
            return 'a2'
        #| | |?|
        #| |O| |
        #|O| | |
        elif cor[2,0]==2 and cor[0,2]==0:
            cor[0,2]=2
            return 'a3'
        #| | | |
        #|O|O|?|
        #| | | |
        elif cor[1,0]==2 and cor[1,2]==0:
            cor[1,2]=2
            return 'b3'
        
        #Defend
        else:
        
            #|X|O|X|
            #| | | |
            #| | | |
            if 'a1' in player_action and 'a3' in player_action and cor[0,1]==0:
                cor[0,1]=2
                return 'a2'
            #|X| | |
            #|O| | |
            #|X| | |
            elif 'a1' in player_action and 'c1' in player_action and cor[1,0]==0:
                cor[1,0]=2
                return 'b1'
            #| | | |
            #| | | |
            #|X|O|X|
            elif 'c3' in player_action and 'c1' in player_action and cor[2,1]==0:
                cor[2,1]=2
                return 'c2'
            #| | |X|
            #| | |O|
            #| | |X|
            elif 'a3' in player_action and 'c3' in player_action and cor[1,2]==0:
                cor[1,2]=2
                return 'b3'
            
            #Two stick together
            
            #|X|X|O|
            #| | | |
            #| | | |
            elif 'a1' in player_action and 'a2' in player_action and cor[0,2]==0:
                cor[0,2]=2
                return 'a3'
            #|O|X|X|
            #| | | |
            #| | | |
            elif 'a2' in player_action and 'a3' in player_action and cor[0,0]==0:
                cor[0,0]=2
                return 'a1'
            #|X| | |
            #|X| | |
            #|O| | |
            elif 'a1' in player_action and 'b1' in player_action and cor[2,0]==0:
                cor[2,0]=2
                return 'c1'
            #|O| | |
            #|X| | |
            #|X| | |
            elif 'b1' in player_action and 'c1' in player_action and cor[0,0]==0:
                cor[0,0]=2
                return 'a1'
            #| | | |
            #| | | |
            #|X|X|O|
            elif 'c2' in player_action and 'c1' in player_action and cor[2,2]==0:
                cor[2,2]=2
                return 'c3'
            #| | | |
            #| | | |
            #|O|X|X|
            elif 'c2' in player_action and 'c3' in player_action and cor[2,0]==0:
                cor[2,0]=2
                return 'c1'
            #| | |X|
            #| | |X|
            #| | |O|
            elif 'a3' in player_action and 'b3' in player_action and cor[2,2]==0:
                cor[2,2]=2
                return 'c3'
            #| | |O|
            #| | |X|
            #| | |X|
            elif 'b3' in player_action and 'c3' in player_action and cor[0,2]==0:
                cor[0,2]=2
                return 'a3'
            
            #Player take useless move. Attack!
            else:
                while True:
                    choose2=random.randint(1,8)
                    if choose2==1:
                        if cor[0,0]==0:
                            cor[0,0]=2
                            return 'a1'
                    elif choose2==2:
                        if cor[0,1]==0:
                            cor[0,1]=2
                            return 'a2'
                    elif choose2==3:
                        if cor[0,2]==0:
                            cor[0,2]=2
                            return 'a3'
                    elif choose2==4:
                        if cor[1,2]==0:
                            cor[1,2]=2
                            return 'b3'
                    elif choose2==5:
                        if cor[2,2]==0:
                            cor[2,2]=2
                            return 'c3'
                    elif choose2==6:
                        if cor[2,1]==0:
                            cor[2,1]=2
                            return 'c2'
                    elif choose2==7:
                        if cor[2,0]==0:
                            cor[2,0]=2
                            return 'c1'
                    else:
                        if cor[1,0]==0:
                            cor[1,0]=2
                            return 'b1'

    #Player took the middle
    #Must defend, cannot attack because all possible is needed to defend
    else:
        #if not the first move, may be able to attack
        formation=[(0,0),(0,1),(0,2)]
        #|O|O|?|
        #| | | |
        #| | | |
        if cor[formation[0]]==2 and cor[formation[1]]==2 and cor[formation[2]]==0:
            cor[formation[2]]=2
            return 'a3'
        #|O|?|O|
        #| | | |
        #| | | |
        elif cor[formation[0]]==2 and cor[formation[1]]==0 and cor[formation[2]]==2:
            cor[formation[1]]=2
            return 'a2'
        #|?|O|O|
        #| | | |
        #| | | |
        elif cor[formation[0]]==0 and cor[formation[1]]==2 and cor[formation[2]]==2:
            cor[formation[0]]=2
            return 'a1'
        
        formation=[(0,2),(1,2),(2,2)]
        #| | |O|
        #| | |O|
        #| | |?|
        if cor[formation[0]]==2 and cor[formation[1]]==2 and cor[formation[2]]==0:
            cor[formation[2]]=2
            return 'c3'
        #| | |O|
        #| | |?|
        #| | |O|
        if cor[formation[0]]==2 and cor[formation[1]]==0 and cor[formation[2]]==2:
            cor[formation[1]]=2
            return 'b3'
        #| | |?|
        #| | |O|
        #| | |O|
        if cor[formation[0]]==0 and cor[formation[1]]==2 and cor[formation[2]]==2:
            cor[formation[0]]=2
            return 'a3'
        
        formation=[(2,2),(2,1),(2,0)]
        #| | | |
        #| | | |
        #|?|O|O|
        if cor[formation[0]]==2 and cor[formation[1]]==2 and cor[formation[2]]==0:
            cor[formation[2]]=2
            return 'c1'
        #| | | |
        #| | | |
        #|O|?|O|
        if cor[formation[0]]==2 and cor[formation[1]]==0 and cor[formation[2]]==2:
            cor[formation[1]]=2
            return 'c2'
        #| | | |
        #| | | |
        #|O|O|?|
        if cor[formation[0]]==0 and cor[formation[1]]==2 and cor[formation[2]]==2:
            cor[formation[0]]=2
            return 'c3'
        
        formation=[(0,2),(0,1),(0,0)]
        #|?| | |
        #|O| | |
        #|O| | |
        if cor[formation[0]]==2 and cor[formation[1]]==2 and cor[formation[2]]==0:
            cor[formation[2]]=2
            return 'a1'
        #|O| | |
        #|?| | |
        #|O| | |
        if cor[formation[0]]==2 and cor[formation[1]]==0 and cor[formation[2]]==2:
            cor[formation[1]]=2
            return 'b1'
        #|O| | |
        #|O| | |
        #|?| | |
        if cor[formation[0]]==0 and cor[formation[1]]==2 and cor[formation[2]]==2:
            cor[formation[0]]=2
            return 'c1'
        
        #Defend
        
        #|X| | |
        #| |X| |
        #| | |O|
        elif 'a1' in player_action and cor[2,2]==0:
            cor[2,2]=2
            return 'c3'
        #| |X| |
        #| |X| |
        #| |O| |
        elif 'a2' in player_action and cor[2,1]==0:
            cor[2,1]=2
            return 'c2'
        #| | |X|
        #| |X| |
        #|O| | |
        elif 'a3' in player_action and cor[2,0]==0:
            cor[2,0]=2
            return 'c1'
        #| | | |
        #|O|X|X|
        #| | | |
        elif 'b3' in player_action and cor[1,0]==0:
            cor[1,0]=2
            return 'b1'
        #|O| | |
        #| |X| |
        #| | |X|
        elif 'c3' in player_action and cor[0,0]==0:
            cor[0,0]=2
            return 'a1'
        #| |O| |
        #| |X| |
        #| |X| |
        elif 'c2' in player_action and cor[0,1]==0:
            cor[0,1]=2
            return 'a2'
        #| | |O|
        #| |X| |
        #|X| | |
        elif 'c1' in player_action and cor[0,2]==0:
            cor[0,2]=2
            return 'a3'
        #| | | |
        #|X|X|O|
        #| | | |
        elif 'b1' in player_action and cor[1,2]==0:
            cor[1,2]=2
            return 'b3'

def checking():
    #|?|?|?|
    #| | | |
    #| | | |
    check=[(0,0),(0,1),(0,2)]
    if cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]==cor[check[1]]==cor[check[2]]:
        return True
    #| | |?|
    #| | |?|
    #| | |?|
    check=[(0,2),(1,2),(2,2)]
    if cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]==cor[check[1]]==cor[check[2]]:
        return True
    #| | | |
    #| | | |
    #|?|?|?|
    check=[(2,0),(2,1),(2,2)]
    if cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]==cor[check[1]]==cor[check[2]]:
        return True
    #|?| | |
    #|?| | |
    #|?| | |
    check=[(0,2),(0,1),(0,0)]
    if cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]==cor[check[1]]==cor[check[2]]:
        return True
    #|?| | |
    #| |?| |
    #| | |?|
    check=[(0,0),(1,1),(2,2)]
    if cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]==cor[check[1]]==cor[check[2]]:
        return True
    #| |?| |
    #| |?| |
    #| |?| |
    check=[(0,1),(1,1),(2,1)]
    if cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]==cor[check[1]]==cor[check[2]]:
        return True
    #| | |?|
    #| |?| |
    #|?| | |
    check=[(0,2),(1,1),(2,0)]
    if cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]==cor[check[1]]==cor[check[2]]:
        return True
    #| | | |
    #|?|?|?|
    #| | | |
    check=[(1,0),(1,1),(1,2)]
    if cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]!=0 and cor[check[0]]==cor[check[1]]==cor[check[2]]:
        return True

def single_player():
    print('|a1|a2|a3|\n|b1|b2|b3|\n|c1|c2|c3|')
    #Round 1
    marking(0)
    showcase()
    print('The computer has mark %s.'%compStart())
    showcase()
    
    #Round 2
    while True:
        marking(0)
        showcase()
        if checking():
            print('Congrats! You won!')
            break
        if 0 not in cor:
            print('It\'s a draw!')
            break
        print('The computer has mark %s.'%comp())
        showcase()
        if checking():
            print('Too bad. Computer won.')
            break
        if 0 not in cor:
            print('It\'s a draw!')
            break
    print('Game over!')

def two_player():
    global name1, name2
    name1=input('Player 1, please input your name: ')
    name2=input('Player 2, please input your name: ')
    print(name1,'vs',name2)
    print('|a1|a2|a3|\n|b1|b2|b3|\n|c1|c2|c3|')
    while True:
        marking(1)
        showcase()
        if checking():
            print(name1,'won!')
            break
        if 0 not in cor:
            print('It\'s a draw!')
            break
        marking(2)
        showcase()
        if checking():
            print(name2,'won!')
            break
        if 0 not in cor:
            print('It\'s a draw!')
            break
    print('Game over!')
    

#Menu
mode='0'
print('Welcome to Tic Tac Toe!')
while mode!='1' or mode!='2':
    print('1. Single Player')
    print('2. Two player')
    mode=input('Please choose a mode: ')
    if mode=='1':
        single_player()
        break
    elif mode=='2':
        two_player()
        break
    else:
        print('Please select mode by typing 1 or 2.')
