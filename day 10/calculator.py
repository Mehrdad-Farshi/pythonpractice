    # add
def add (n1,n2):
    '''n1 + n2'''
    return n1 + n2
    # substracte
def sub(n1,n2):
    '''n2 - n1'''
    return n2 - n1
    # multiple
def multiple(n1,n2):
    '''n1 * n2'''
    return n1 * n2
    # divide
def devide (n1,n2):
    '''n1 / n2'''
    return n1 / n2

opration= {
    '+':add,
    '-':sub,
    '/':devide,
    '*':multiple,
}
def calc(num1,num2):
    func = opration[opration_symb]
    return func(num1,num2)
calc_continue =True
while(calc_continue):
    num1 = int(input('what the firts number ? :'))
    for symb in opration :
        print (symb)
    num2 = int(input('what the sec   number ? :'))
    opration_symb = input('pick an opration from above : ')
    answear1 = calc(num1,num1)
    state = input('do you want to continue y or n ? ')
    if state == 'n' : 
        calc_continue = False
    



print(f'{num1} {opration_symb} {num2} = {calc(num1,num2)}')