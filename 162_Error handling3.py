while True:
    try:
        age=int(input('what is your age?'))
        10/age
        raise ValueError('hey cut it out')
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
        
        
# error are unavoidable as a programmeur, we have to enticipate these bugs
