def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

# Now we can use both *args ,**kwargs to pass arguments to this function :
myFun('python', 'with', 'pranshu', first="Python", mid="with", last="Pranshu")