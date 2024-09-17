# if & else if statements
def max2(x, y):
    '''
    (float, float) --> float
    retourne la val max
    '''

    # vaiables
    m = y

    # if x greater than y
    if x > y :
        m = x

    # # x is less than y
    # else:
    #     m = y

    # print result
    print("m =", m)

# user input
x = float(input("Number please: "))
y = float(input("Another number please: "))

# calling function passing the user input
max2(x,y)
