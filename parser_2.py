Terminals = ['+','*','int',')','(','$']
var = ['E','T','x','Y']
Grammer = [['E',['T','X']],['T',['int','Y']],['T',['(','E',')']], ['X',['+','E']], ['X',[]], ['Y',['*','T']], ['Y',[]]]
Parsing_table_shift= { ( 0,'(' ) : 4,( 0,'int' ) : 3,( 2,'+' ) : 6,( 3,'*' ) : 8,( 4,'(' ) : 4,( 4,'int' ) : 3,
                       ( 6,'(' ) : 4,( 6,'int' ) : 3,( 8,'(' ) : 4,( 8,'int' ) : 3,( 9,')' ) : 11}
Parsing_table_reduce= { ( 2,')' ) : 5, ( 2,'$' ) : 5,( 3,'+' ) : 7,( 3,')' ) : 7,( 3,'$' ) : 7,( 5,')' ) : 1,
                       ( 5,'$' ) : 1,( 7,'+' ) : 2,( 7,')' ) : 2,( 7,'$' ) : 2,( 10,')' ) : 4, ( 10,'$' ) : 4,
                       ( 11,'+' ) : 3,( 11,')' ) : 3,( 11,'$' ) : 3,( 12,'+' ) : 6,( 12,')' ) : 6,( 12,'$' ) : 6}
Parsing_table_goto= { (0,'E') : 1, ( 0,'T' ) : 2,( 3,'Y' ) : 7,( 4,'E' ) : 9,( 4,'T' ) : 2,( 6,'E' ) : 11,
                       ( 6,'T' ) : 2,( 8,'T' ) : 12, ( 2,'X' ) : 5}
Parsing_table_Accept= { (1 , '$') : 'Accept'}
stack=[0]
p = 'No'
def shift(a,stack,input):
    stack.append(input[0])
    input.remove(input[0])
    stack.append(a)
    return input,stack
def reduce(b ,stack,input , Grammer,Parsing_table_goto):
    i = len(Grammer[b - 1][1]) * 2
    while i != 0:
        stack.pop()
        i = i - 1
    stack.append(Grammer[b - 1][0])
    c = Parsing_table_goto.get((stack[-2], stack[-1]), 'null')
    if c != 'null':
        goto(c, stack)
    else:
        p = 'No'
    return input, stack
def goto(c, stack):
    stack.append(c)
    return stack

input = input("enter your string : ").split()
input.append('$')

while p != 'Yes':
    a = Parsing_table_shift.get((stack[-1], input[0]), 'null')
    if a != 'null':
        shift(a,stack,input)
    else:
        b = Parsing_table_reduce.get((stack[-1], input[0]), 'null')
        if b != 'null':
            reduce(b ,stack,input , Grammer,Parsing_table_goto)
        else:
            c = Parsing_table_goto.get((stack[-1], input[0]), 'null')
            if c != 'null':
                goto(c, stack)
            else:
                d = Parsing_table_Accept.get((stack[-1], input[0]), 'null')
                if d != 'null':
                    p = 'Yes'
                    input.remove(input[0])
                else: p = 'No'
                break
print(p)