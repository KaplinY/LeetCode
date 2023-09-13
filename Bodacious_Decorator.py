import math

def make_pretty(func):

    def inner(a,b,c):
        print("Function: ",a,"x^2+",b,"x+",c," has following solutions:")
        return func(a,b,c)
    return inner

@make_pretty
def eq_solver(a,b,c):
    d = b*b - 4*a*c
    if d < 0:
        return "No real solutions"
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    return x1,x2


a,b,c = 1,4,3
print(eq_solver(a,b,c))  