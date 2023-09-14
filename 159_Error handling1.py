age = input('what is your age')
print(age)

# if input AC so can add int in front but still if I put AC instead a numb "ValueError"

# how to fix it?


try:
    age = int(input('what is your age?'))
    print(age)
except:
    print('please enter a number')

# if stop there than have to restart the program, so make it run automatically, have to use a while loop

while True:
    try:
        age = int(input('what is your age?'))
        print(age)
    except:
        print('please enter a number')
        
# this time I still continue to ask your age even if u enter a numb
# need to "break" once your enter a num

while True:
    try:
        age = int(input('what is your age?'))
        print(age)
    except:
        print('please enter a number')
    else:
        print('thank you')
        break


# if we do 
while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except:
        print('please enter a number')
    else:
        print('thank you')
        break

# program continue to ask to enter a numb even after entering "0",

while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
    else:
        print('thank you')
        break
    
# so we can add an ValueError but in this case the exception accept only that error and not other error so what to do?

# then have to add another exception
while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you')
        break
    
# What happened if add another "ValueErro"
while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
    except ValueError:
        print('!!!!!!!!!!!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you')
        break
    
# it will work just one