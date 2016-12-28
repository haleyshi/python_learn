__author__ = 'eguoshi'

turn = "X"
maps = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
done = False

def print_board():
    for i in range(0, 3):
        for j in range(0, 3):
            print maps[2-i][j],
            if j != 2:
                print "|",
        print ""


def check_done():
    for i in range(0,3):
        if maps[i][0] == maps[i][1] == maps[i][2] != " " \
                or maps[0][i] == maps[1][i] == maps[2][i] != " ":
            print turn, "won!!!"
            return True

    if maps[0][0] == maps[1][1] == maps[2][2] != " " \
            or maps[2][0] == maps[2][1] == maps[0][2] != " ":
        print turn, "won!!!"
        return True

    if " " not in maps[0] and " " not in maps[1] and " " not in maps[2]:
        print "Draw!!!"
        return True

    return False
print "Chessboard: "
print "7|8|9"
print "4|5|6"
print "1|2|3"
print

while not done:
    print turn, "'s turn***"
    print_board()
    print

    moved = False
    while not moved:
        print "Please select position by typing a number between 1 and 9," \
              "see top for which number that is which position..."

        try:
            pos = input("Select: ")
            if pos in range(1, 10):
                Y = pos/3
                X = pos%3

                if X != 0:
                    X -= 1
                else:
                    X = 2
                    Y -= 1

                if maps[Y][X] != " ":
                    print "Position Not Empty!!!"
                else:
                    maps[Y][X] = turn
                    moved = True
                    done = check_done()

                    if not done:
                        if turn == "X":
                            turn = "O"
                        else:
                            turn = "X"

        except:
            print "Please input an numeric value!"
