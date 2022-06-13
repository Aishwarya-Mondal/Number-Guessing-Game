
operator_list = ['+','-','*','/']
#precedence_chart = {'/': 1,'*': 1,'+': 0,'-': 0}

def add(user_input):
    global operator_list
    sum=0
    for x in user_input:
        if x not in operator_list:
            sum += int(x)
    return sum

def subtract(user_input):
    global operator_list
    sub=int(user_input[0])
    for x in user_input:
        if x not in operator_list and user_input.index(x)!=0:
            sub -= int(x)
    return sub

def multiply(user_input):
    global operator_list
    mult = 1
    for x in user_input:
        if x not in operator_list:
            mult *= int(x)
    return mult

def divide(user_input):
    global operator_list
    div=int(user_input[0])
    for x in user_input:
        if x not in operator_list and user_input.index(x)!=0:
            div /= int(x)
    return div


def start_calculator():
    res = 0
    print("----Welcome to my Calculator----")
    print("Enter your operation:")
    user_input = input()

    if '+' in user_input and '*' not in user_input and '-' not in user_input and '/' not in user_input:
        res = add(user_input)
    
    elif '-' in user_input and '*' not in user_input and '+' not in user_input and '/' not in user_input:
        res = subtract(user_input)
    
    elif '*' in user_input and '+' not in user_input and '-' not in user_input and '/' not in user_input:
        res = multiply(user_input)
    
    elif '/' in user_input and '*' not in user_input and '-' not in user_input and '+' not in user_input:
        res = divide(user_input)

    else:
        print("please provide either '+' or '-' or '*' or '/'.")

    print("Result: ",res)


if __name__ == '__main__':
    start_calculator()