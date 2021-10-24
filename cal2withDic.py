while 1:
    num1 = float(input("input num1: "))
    num2 = float(input("input num2: "))
    operator = input("input operator: ")

    d = {
        "+": num1+num2,
        "-": num1-num2,
        "*": num1*num2,
        "/": num1/num2,
        "%": num1%num2,
    }
# har adadi true va 0 false ->age hasel javab 0 she 
# mishe false va khorab mere:/

    if d.get(operator,False):
        print(d[operator])
    else:
        if d[operator]==0:
            print (0)
        else:
            print("operator is not valied!! ")

