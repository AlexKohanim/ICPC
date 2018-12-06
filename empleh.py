#!/usr/bin/env python3

# not finished as of 10/6/18

out = """+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+ """

def place_pieces(moves, out, white=True):
    # mult pos by 2 and sub 1
    print(moves)
    if ":" in moves:
        return out
    board = out.split("\n")
    for m in moves:
        piece = ""
        col = 0
        row = 0
        if len(m) == 2:
            piece = "P"
        else:
            piece = m[0]
            m = m[1:]
        col = ord(m[0]) - ord('a') +1
        row = (int(m[1])* 2) - 1

        edit_row = board[row]
        edit_row = edit_row[0:4*col - 2] + piece + edit_row[4*col - 1:]
        #print(edit_row)
        board[row] = edit_row
    out = "\n".join(board)
    return out

        
        




whites = input()#.split()[1].split(",")
if "," in whites:
    whites = whites.split()[1].split(",")
blacks = input()#.split()[1].split(",")
if "," in blacks:
    blacks = blacks.split()[1].split(",")

out = place_pieces(whites, out, True)
out = place_pieces(blacks, out, False)

print(out)
