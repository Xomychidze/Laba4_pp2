def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

<<<<<<< HEAD
print(myfunc1())  
=======
print(myfunc1()) 
>>>>>>> 933d7a6 (8 commit)
