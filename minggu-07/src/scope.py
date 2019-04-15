def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print ("after local assigment", spam)
    do_nonlocal()
    print ("after nonlocal assigment", spam)
    do_global()
    print ("after global assigment", spam)

scope_test()
print ("in global scope :", spam)