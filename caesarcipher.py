alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#   =''
state = True
while (state):
    word=''
    text = input('place your text here  :').lower()
    func = input('what function you want enc or dec ?').lower()
    hash = int(input('what is hash :'))
    def ceser(text,func,hash):
        global word
        if func =='enc':
            for ch in text :
                alphaplace = alphabet.index(ch)
                if hash+alphaplace >= len(alphabet) :
                    word+=alphabet[hash+alphaplace - len(alphabet)]
                else:
                   word+=alphabet[alphaplace+hash]
        else:
            for ch in text:
                alphaindex = alphabet.index(ch)
                word+=alphabet[alphaindex - hash]
        return word

    print(ceser(text=text,func=func,hash=hash))
    # the while loop keep asking user if they want to do it again
    quest=True
    while(quest):
        textstate=input('do you want to start again Y/n ? ').lower()
        if textstate =='n' or textstate =='no':
            state = False
            quest=False
            print('good bye')
        if textstate =='' or textstate=='Y' or  textstate=='yes':
            quest=False
        else:
            print('try again')
            