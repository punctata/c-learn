
n = 2
chosen = [False] * n
permutation = []

def oo(x):
    if x == 1:return "st"
    elif x == 2 :return "nd"
    elif x== 3: return "rd"
    else : return "th"

def search1():
    print "entering search for selecting the ", len(permutation) + 1, oo(len(permutation) + 1), "element .."
    if len(permutation) == n:
        print permutation
    else:
        for i in range(0, n):
            print "trying selecting the ", len(permutation) + 1, oo(len(permutation) + 1), "element to be", i
            if chosen[i]:
                print "but it is already chosen"
                continue
            chosen[i] = True
            permutation.append(i)
            print "added ", i, " now we have", permutation
            search2()
            chosen[i] = False
            permutation.pop()
            print "removed ", i, " now we have", permutation
    print "exiting search for selecting the ", len(permutation) + 1, oo(len(permutation) + 1), "element .."


def search2():
    print "entering search for selecting the ", len(permutation) + 1, oo(len(permutation) + 1), "element .."
    if len(permutation) == n:
        print permutation
    else:
        for i in range(0, n):
            print "trying selecting the ", len(permutation) + 1, oo(len(permutation) + 1), "element to be", i
            if chosen[i]:
                print "but it is already chosen"
                continue
            chosen[i] = True
            permutation.append(i)
            print "added ", i, " now we have", permutation
            search3()
            chosen[i] = False
            permutation.pop()
            print "removed ", i, " now we have", permutation
    print "exiting search for selecting the ", len(permutation) + 1, oo(len(permutation) + 1), "element .."


def search3():
    print "entering search3 for selecting the ", len(permutation) + 1, oo(len(permutation) + 1), "element .."
    print permutation
    print "exiting search3 for selecting the ", len(permutation) + 1, oo(len(permutation) + 1), "element .."
    

search()

