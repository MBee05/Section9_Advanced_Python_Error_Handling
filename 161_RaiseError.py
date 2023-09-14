# Error handling

while True:
    try:
        age=int(input('what is your age?'))
        10/age
    except ValueError:
        print(('pls enter a number'))
    except ZeroDivisionError:
        print('pls enter age higher than 0')
    else:
        print('thx!')
        break    
    finally:
        print('ok, done')
        
        # ****************
        
while True:
    try:
        age=int(input('what is your age?'))
        10/age
    except ValueError:
        print(('pls enter a number'))
        continue
    except ZeroDivisionError:
        print('pls enter age higher than 0')
        break
    else:
        print('thx!')
        break    
    finally:
        print('ok, done')
        
        
        # *****************
        
while True:
    try:
        age=int(input('what is your age?'))
        10/age
    except ValueError:
        print(('pls enter a number'))
        continue
    except ZeroDivisionError:
        print('pls enter age higher than 0')
        break
    else:
        print('thx!')
    finally:
        print('ok, done')