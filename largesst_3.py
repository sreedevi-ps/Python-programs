def large(a,b,c):
    if(a>b and a>c):
        print("{0} is the greatest among {0},{1},{2} ".format(a,b,c))
    elif(b>a and b>c):
        print("{0} is the greatest among {0},{1},{2} ".format(b,a,c))
    else:
        print("{0} is the greatest among {0},{1},{2} ".format(c,a,b))
large(20,30,4)