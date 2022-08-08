    # add
def add (n1,n2):
    '''n1 + n2'''
    return n1 + n2
    # substracte
def sub(n1,n2):
    '''n2 - n1'''
    return n1 - n2
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
def calculator():   
    def calc(num1,num2):
        func = opration[opration_symb]
        return func(num1,num2)

    num1 = float(input('what the firts number ? :'))
    for symb in opration :
        print (symb)
    opration_symb = input('pick an opration from above : ')
    num2 = float(input('what the sec   number ? :'))
    answear1 = calc(num1,num2)
    print(f'{num1} {opration_symb} {num2} = {answear1}')

    # calc_continue =True
    while(True):
        state= input('are you wish to continue ? y or n : ') 
        if state == 'n' :
            # calc_continue = False
            break
            calculator()
        else:
            for symb in opration :
                print (symb)
        opration_symb = input('pick an opration from above : ')
        print(f'{answear1} {opration_symb}')
        num3 = float(input('what the third   number ? :'))
        answear2 = calc(answear1,num3)
        print(f'{answear1} {opration_symb} {num3} = {answear2}')
        answear1 = answear2
calculator()