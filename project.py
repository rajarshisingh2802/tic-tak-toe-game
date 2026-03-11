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

class players:

    def __init__(self):
        self.fields = ["Name","symbol","track"]
        self.records = []

    def add(self,records):
        self.records.extend(records)

    def display(self):
        return f"Player Name : {self.records[self.fields.index("Name")]}, symbol : {self.records[self.fields.index("symbol")]}"
    
    @staticmethod
    def welcome():
        return "Hello player\nWelcome to Tic-Tac-Toe\nplease enter the following info:"
    
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
            
    def won(self):
        if len(self.records[2]) < 3:
            return None
        
        l = self.records[2]
        l.sort(reverse=True)
        diff = []
        for i in range(len(self.records[2]) - 1):
            diff.append(l[i] - l[i+1])
        
        for i in range(len(diff) - 1):
            if diff[i] == diff[i+1] and diff[i] != 2:
                return True
            elif l[-1] == 3 and diff[i] == diff[i+1] and diff[i] == 2:
                return True
                
        return None

        
#-------------------------------------------------------#
'''Actual game play'''
#-------------------------------------------------------#

print(players.welcome())

#player 1
name1 = str(input("Enter your name as player 1: "))
symbol1 = str(input("Choose your symbol: "))
track1 = []
p1 = players()
p1.add([name1,symbol1,track1])

#player 2
name2 = str(input("Enter your name as player 2: "))
symbol2 = str(input("Choose your symbol: "))
track2 = []
p2 = players()
p2.add([name2,symbol2,track2])

print("Game Starts")
print("Sample for reference:")
Grid.show_sample()

i = 0
while i < 9:

    #player 1
    if i % 2 == 0:
        print("Player 1 Your turn")
        val1 = players.get_val()
        Grid.change(val1,p1.records[p1.fields.index("symbol")])
        Grid.show()
        p1.records[2].append(val1)

        #check
        if p1.won() == True:
            print("Player 1 Won !!!!!!")
            break

    else:
        print("Player 2 Your turn")
        val2 = players.get_val()
        Grid.change(val2,p2.records[p2.fields.index("symbol")])
        Grid.show()
        p2.records[2].append(val2)
        
        #check
        if p2.won() == True:
            print("Player 2 Won !!!!!!")
            break
    i += 1

if i >= 9:
    print("Its a tie")

print("Hope you liked it")