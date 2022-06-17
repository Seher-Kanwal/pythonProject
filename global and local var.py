l = 34


def seher():
    # if we did not define a local var, then the global var is read only
    # we can't modify this, in order to change we use global keyword to give permissions
    global l
    l = l + 23
    print(l)


seher()


def fn1():
    x = 23

    def fn2():
        # this will look outside int the main program, no var found, so its created a var and store its value
        global x
        x = 34

    print("Before calling fn2, given more preference to local var:", x)
    fn2()
    print("after calling fn2, given more preference to local var:", x)

fn1()
print("as fn2 create a global var so value is: ", x)
