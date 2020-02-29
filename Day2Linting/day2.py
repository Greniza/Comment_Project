'''
I'm really sorry if this isn't linted properly.
I can't get the linter downloaded.
'''
def is_float(x):
    '''
    takes in string, returns true if string is of format ####, ##.#, -#.#, or -###.
    else returns false. returns false with -.
    '''
    periodcount = 0
    if not x:
        return False
    if x[0] == '-':
        if x.replace('.','') == '-':
            return False
        x = x[1:]
    for pos in x:
        if pos == '.' and periodcount == 0:
            periodcount = 1
        elif pos not in ('1','2','3','4','5','6','7','8','9','0'):
            return False
    return True


def largest(nl):
    '''max() but mine'''
    themax = nl[0]
    for num in nl:
        if num > themax:
            themax = num
    return themax


def userlargest():
    '''returns largest integer of inputs provided by user'''
    while True:
        ui = input('List of numbers seperated by spaces ').split(' ')
        q = True
        for num in ui:
            if not is_float(num):
                q = False
        if q:
            break
    ui = [float(x) for x in ui]
    return largest(ui)


def filelargest():
    '''reads lotsofnumbers.txt, returns largest number'''
    file = open('lotsofnumbers.txt', 'r').readlines()
    file = [line.strip().split(' ') for line in file]
    intlist = [[int(x) for x in line] for line in file]
    # actually kind of proud of that list argument
    return largest(intlist)


def main():
    print(largest([-5, 2, 7, 9, 11, 3, -1]))
    print(userlargest())
    print(filelargest())


if __name__ == '__main__':
    main()
