#Lexical Analyzer
keywords = ['int', 'double', 'get', 'print', 'if', 'else', 'for']
separators = ['(', ')', '{', '}', ';']
logic_operators = ['==', '!=', '<=', '<', '>=', '>']
math_operators = ['=', '/', '-', '*', '+', '++']
digits=[str(i) for i in range(10)]
characters=[chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]


token_class = {
    'double':'DOUBLE',
    'int':'INT',
    'get':'GET',
    'print':'PRINT',
    'if':'IF',
    'else':'ELSE',
    'for':'FOR',
    '(':'OPENPARENTHESIS',
    ')':'CLOSEPARENTHESIS',
    '{':'OPENCURLYBRACE',
    '}':'CLOSECURLYBRACE',
    ';':'SEMI-COLON'

}



# در این بخش ادرس فایل تکست روی سیستم خودتان باید قرار بگیرد تا کد اجرا شود
with open('E:/0دانشگاه0/کامپایلر/campiler_project/input.txt', 'r') as file:
    input = file.read()
def LexicalAnalyzer(input):
    tokens = []
    pointer0 = 0

    while pointer0 < len(input):
        #POINTER TO THE CURRENT CHARACTER
        char = input[pointer0]

        #COMMENTs
        if char == '\\' and input[pointer0+1] == '*':
            pointer0 += 1
            while pointer0 < len(input) and not (input[pointer0] == '*' and input[pointer0+1] == '\\'):
                pointer0 += 1
            pointer0 +=2

            continue


        #WHITE SPACEs
        if char.isspace():
            pointer0 += 1
            continue


        # SEPERATORs
        if char in separators:
            tokens.append((char, token_class[char]))
            pointer0 += 1
            continue


        #LOGIC_OPERATORs
        if char in logic_operators:
            if pointer0+1 < len(input) and input[pointer0+1] in logic_operators and char + input[pointer0+1] in logic_operators:
                tokens.append((char+f'{input[pointer0+1]}', 'LOGIC_OPERATOR'))
                pointer0 += 2
            else:
                tokens.append((char, 'LOGIC_OPERATOR'))
                pointer0 += 1
            continue


        #MATH_OPERATORs
        if char in math_operators :
            if pointer0+1 < len(input) and input[pointer0+1] in math_operators and char + input[pointer0+1] in math_operators:
                tokens.append((char+f'{input[pointer0+1]}', 'MATH_OPERATOR'))
                pointer0 += 2
            else:
                tokens.append((char, 'MATH_OPERATOR'))
                pointer0 += 1
            continue




        #KEYWORDs/IDs
        if char in characters:
            pointer1 = pointer0 + 1
            while pointer1 < len(input) and input[pointer1] in (characters or digits):
                pointer1 += 1

            word = input[pointer0:pointer1]

            if word in keywords:
                tokens.append((word, token_class[word]))
            else:
                tokens.append((word, 'IDENTIFIER'))
            pointer0 = pointer1
            continue


        #INTs and DOUBLEs   
        if char in digits:
            if char == "0" :
                tokens.clear()
                tokens.append(('NUMBER DEFINITION ERROR', 'ERROR'))
                return tokens
            pointer1 = pointer0 + 1
            has_dot = False
            while pointer1 < len(input) and (input[pointer1] in digits or input[pointer1] == '.'):
                if input[pointer1] == '.':
                    has_dot=True
                pointer1 += 1
            number = input[pointer0:pointer1]
            number_of_dot = number.count('.')

            if has_dot:
                if input[pointer1-1] == '.':
                    tokens.clear()
                    tokens.append(('END NUMBER WITH DOT', 'ERROR'))
                    return tokens
                if number_of_dot > 1 :
                    tokens.clear()
                    tokens.append(('MORE THAN ONE DOT IN NUMBER', 'ERROR'))
                    return tokens  
                tokens.append((input[pointer0:pointer1], 'DOUBLE'))
            else:
                tokens.append((input[pointer0:pointer1], 'INT'))
            pointer0 = pointer1
            continue
            
        #STRINGs
        if char == '"':
            pointer1 = pointer0 + 1
            while pointer1 < len(input) and input[pointer1] != '"' and input[pointer1] != '\n':
                pointer1 += 1
            if pointer1 < len(input) and input[pointer1] == '"':
                tokens.append((input[pointer0:pointer1+1], 'STRING'))
                pointer0 = pointer1 + 1
            else:
                tokens.clear()
                tokens.append(('STRING DEFINITION ERROR', 'ERROR'))
                return tokens
            continue
        
        else:
            tokens.clear()
            tokens.append(('INVALID DATA', 'ERROR'))
            return tokens
    return tokens




tokens = LexicalAnalyzer(input)

with open('E:/0دانشگاه0/کامپایلر/compiler proj/phase1/implementation/output.txt', 'w') as file:
    for token in tokens:
        file.write(f'<{token[1]}, "{token[0]}">\n')


for token in tokens:
    print(token)