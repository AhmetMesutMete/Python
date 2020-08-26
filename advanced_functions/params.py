def sum(a,b):
    return a+b
def exct(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def operation(f1, f2, f3, f4, OpName):
    if OpName == "sum":
        print(f1(2,3))
    elif OpName == "exct":
        print(f2(5,3))
    elif OpName == "mul":
        print(f3(3,4))
    elif OpName == "div":
        print(f4(4,10)) 
    else: 
        print("invalid operation")    

operation(sum,exct,mul,div,"sum")
operation(sum,exct,mul,div,"exct")
operation(sum,exct,mul,div,"mul")
operation(sum,exct,mul,div,"div")
