#1 - The grid
class Grid:

    l = [" "]*9
    s = [1,2,3,4,5,6,7,8,9]

    @staticmethod
    def show():

        k = 0
        #for even lines the first and for odd the second
        for j in range(5):
            
            # 1 - _ | _ | _
            if j % 2 == 0:

                for i in range(5):

                    if i % 2 == 0:
                        print(Grid.l[(i + 6*k)//2],end = " ")
                        
                    else:
                        print("|",end = " ")
                print()
                k += 1
        
            else:
                #-----------
                print("-"*10)

    @staticmethod
    def show_sample():

        k = 0
        #for even lines the first and for odd the second
        for j in range(5):
            
            # 1 - _ | _ | _
            if j % 2 == 0:

                for i in range(5):

                    if i % 2 == 0:
                        print(Grid.s[(i + 6*k)//2],end = " ")
                        
                    else:
                        print("|",end = " ")
                print()
                k += 1
        
            else:
                #-----------
                print("-"*10)

    @staticmethod
    def change(pos,val):
        Grid.l[pos - 1] = val

    #magic square
    '''
    8   3   4 
    1   5   9
    6   7   2
    '''
    magic_square = [8,3,4,1,5,9,6,7,2]

class players:

    def __init__(self):
        self.fields = ["Name","symbol","track"]
        self.records = []

    # adding a player record
    def add(self,records):
        self.records.extend(records)

    def display(self):
        return f"Player Name : {self.records[self.fields.index("Name")]}, symbol : {self.records[self.fields.index("symbol")]}"
    
    @staticmethod
    def welcome():
        return "Hello player\nWelcome to Tic-Tac-Toe\nplease enter the following info:"
    
    # for getting value safely checking for occupied places
    @staticmethod    
    def get_val():
        check = True
        while check:
            val = int(input("Enter your position: "))
            if Grid.l[val-1] != " ":
                print("already taken position !enter again!")
            elif val <= 0:
                print("Invalid Input, !Enter Again!")
            else:
                check = False
                return val
    
    def won(self,track):
        n = len(track)
        delta = sum(track) - 15
        match(n):

            case 3:
                if sum(track) == 15:
                    return True
            case 4:
                if delta in track:
                    return True
            case 5:
                sums = []
                for i in range(3):
                    sums.extend(list(map(lambda x:x + track[i],track[i+1:-1])))
                if delta in sums:
                    return True
        
#-------------------------------------------------------#
'''Actual game play'''
#-------------------------------------------------------#

print(players.welcome())

#player 1
print("Player 1:")
name = input("Enter your name: ")
sym = input("Enter your symbol: ")
p1 = players()
p1.add([name,sym,[]])

#player 2
print("Player 2:")
name = input("Enter your name: ")
sym = input("Enter your symbol: ")
p2 = players()
p2.add([name,sym,[]])

print("Game starts ..........")
print("reference grid")
Grid.show_sample()

#gameplay alternating turns
tie = True
for i in range(9):
    if i % 2 == 0:
        print("player 1 your turn:")
        n1 = players.get_val()
        Grid.change(n1,p1.records[1])
        Grid.show()
        p1.records[2].append(Grid.magic_square[n1-1])

        if p1.won(p1.records[2]):
            print(f"{p1.records[0]} won !!!!!")
            tie = False
            break

    else:
        print("player 2 your turn:")
        n2 = players.get_val()
        Grid.change(n2,p2.records[1])
        Grid.show()
        p2.records[2].append(Grid.magic_square[n2-1])

        if p2.won(p2.records[2]):
            print(f"{p2.records[0]} won !!!!!")
            tie = False
            break        

if tie:
    print("Its a tie!")

print("Hope you liked it")