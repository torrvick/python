#expression = "100/4*2-10/4+3*2"
expression = input("Введите выражение для вычисления: ")
def calc(exp):
    if  exp.find("+") == -1 and \
        exp.find("-") == -1 and \
        exp.find("*") == -1 and \
        exp.find("/") == -1:
        return exp
    if exp.find("-") == 0 and expression.count("-") == 1:
        return exp
    else:

        def parse_left(i,num):
            if exp[i-1] in ["+","-","*","/"] or i==0:
                return num
            else:
                num = exp[i-1] + num
                return parse_left(i-1,num)

        def parse_right(i,num):
            if i==len(exp)-1:
                return num
            if exp[i+1] in ["+","-","*","/"]:
                return num
            else:
                num += exp[i+1]
                return parse_right(i+1,num)

        mul_pos = exp.find("*")
        div_pos = exp.find("/")
        if mul_pos != -1 or div_pos != -1:
            if mul_pos == -1:
                pos = div_pos
                left = parse_left(pos,"")
                right = parse_right(pos,"")
                oper = float(left) / float(right)
            elif div_pos == -1:
                pos = mul_pos
                left = parse_left(pos,"")
                right = parse_right(pos,"")
                oper = float(left) * float(right)
            else:
                if mul_pos < div_pos:
                    pos = mul_pos
                    left = parse_left(pos,"")
                    right = parse_right(pos,"")
                    oper = float(left) * float(right)
                else:
                    pos = div_pos
                    left = parse_left(pos,"")
                    right = parse_right(pos,"")
                    oper = float(left) / float(right)
            # print(exp,left,right)
            exp = exp[:pos - len(left)] + str(oper) + exp[pos+len(right)+1:]
            
            return calc(exp)

        add_pos = exp.find("+")
        sub_pos = exp.find("-")
        if sub_pos != -1:
            pos = sub_pos
            left = parse_left(pos,"")
            right = parse_right(pos,"")
            # print(exp,left,right)
            exp = exp[:pos - len(left)] + str(float(left) - float(right)) + exp[pos+len(right)+1:]
            
            return calc(exp)
        if add_pos != -1:
            pos = add_pos
            left = parse_left(pos,"")
            right = parse_right(pos,"")
            # print(exp,left,right)
            exp = exp[:pos - len(left)] + str(float(left) + float(right)) + exp[pos+len(right)+1:]
            
            return calc(exp)

print(f"Результат вычислений равен {calc(expression)}")
