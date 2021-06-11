from typing import final
def expeded_form(x):
    x = str(x)
    expended_blank = []

    for index, itme in enumerate(reversed(x)):
        expended_blank.append(itme('0'*index))
        final = ' + '.join(reversed(expended_blank))

    print(f'Expanded form for {x} is {final}')

 number = input('Enter the number to be expended - ')  
 expeded_form(number)     