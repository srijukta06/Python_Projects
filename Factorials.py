def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1

    fact = 1
    counter = 1
    #while counter <= num:
     #   fact = fact * counter
      #  counter = counter + 1
    #return fact
    return num * factorial(num - 1)
