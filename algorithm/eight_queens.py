size = 8
row_in_cols = []
count = 0

for col in range(0, size):
    row_in_cols.append(-1)

def printCheeseBoard():
    print 'Answer #%d' %count
    # Just rotate 90 degrees for simplity, should be the same
    for col in range(0, size):
        for head in range(0, row_in_cols[col]):
            print '-',
        print '*',
        for head in range(row_in_cols[col]+1, size):
            print '-',
        print
    print

def queens(current_col=0):
    for col in range(0, current_col-1):    # traver the existing chesses, ensure not in the same column
        row_offset = abs(row_in_cols[current_col-1] - row_in_cols[col])
        line_offset = abs(current_col-1-col)
        if row_offset == 0 or row_offset == line_offset:   # same row, or same diagonal line
            return

    if current_col == size:
        global count
        count = count + 1
        #print count, row_in_cols
        printCheeseBoard()
        return

    for row in range(0, size):
        row_in_cols[current_col] = row
        queens(current_col+1)

queens()
