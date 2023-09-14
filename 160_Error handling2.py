# def sum(num1, num2):
#     return num1+num2

# print(sum('1','2'))

# output 12

# print(sum('1',2))
"""TypeError: can only concatenate str (not "int") to str       
PS C:\Users\Mohamed Bee\Desktop\Python_w_Udemy\Section9_Advanced_Python_Error_Handling>"""

# def sum(num1, num2):
#     try:
#         return num1+num2
#     except TypeError:
#         print('pls enter number')
# print(sum('1',2))

"""SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 67-68: truncated \UXXXXXXXX escape      
PS C:\Users\Mohamed Bee\Desktop\Python_w_Udemy\Section9_Advanced_Python_Error_Handling>"""

# *************************************

# def sum(num1, num2):
#     try:
#         return num1+num2
#     except TypeError as err:
#         print('pls enter number' + err)
# print(sum('1',2))


"""SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 67-68: truncated \UXXXXXXXX escape      
PS C:\Users\Mohamed Bee\Desktop\Python_w_Udemy\Section9_Advanced_Python_Error_Handling>"""
# *****

# def sum(num1, num2):
#     try:
#         return num1+num2
#     except TypeError as err:
#         print('pls enter number')
# print(sum(1,'2'))

"""SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 67-68: truncated \UXXXXXXXX escape      
PS C:\Users\Mohamed Bee\Desktop\Python_w_Udemy\Section9_Advanced_Python_Error_Handling>"""



# *****************
# def sum(num1, num2):
#     try:
#         return num1+num2
#     except TypeError as err:
#         print(f'pls enter number{err}')
        
# print(sum(1,'2'))

# output unsupportedoperand type(s) for +:'int' and 'str'
# None

# ******************
def sum(num1, num2):
    try:
        return num1+num2
    except TypeError as err:
        print(err)
        
# print(sum(1,'2'))

# output unsupportedoperand type(s) for +:'int' and 'str'
# None

# ***************************************

# def sum(num1, num2):
#     try:
#         return num1+num2
#     except (TypeError, ZeroDivisionError):
#         print('Oops')

# # output "Oops"

# ****************************************
# def sum(num1, num2):
#     try:
#         return num1/num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)
        
# print(sum(1,0))
# # Division by zero

# print(sum(1,'2'))
# output unsupportedoperand type(s) for +:'int' and 'str'

# ******************
