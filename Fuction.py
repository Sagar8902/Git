# functions

# def calc_sum(a,b):
#     sum = a+b
#     print(sum)
#
# calc_sum(5,6)


# Average of numbers

# def calc_avg(a,b,c):
#     sum = a+b+c
#     print(sum/3)
#
# calc_avg(2,3,5)


list = ["raju","kaju","ram","shyam"]

# def len_list(a):
#     print(len(a))
#
# len_list(list)


# def sing_line(a):
#     for i in a:
#         print(i, end= " ")
#
# sing_line(list)


# n = 5
#
# def calc_fact(n):
#     fact = 10
#     for i in range(1,n+1):
#         fact *= i
#         print(fact)
#
# calc_fact(n)


# usd = int(input("Enter USD currency: "))
#
# def calc_curr(usd):
#     inr = usd*83
#     print(usd,"USD = ", inr,"INR" )
#
# calc_curr(usd)

# num = int(input("Enter number here: "))
# def num_indentifier():
#      if(num % 2 ==0):
#          print("Your number is even")
#      elif(num % 2 == 1):
#          print("Your number is odd")
#
# num_indentifier()

# n = 5
#
# while n >= 1:
#     print(n)
#     n -= 1

def num(n):
    if(n == 0):
        return
    print(n)
    num(n-1)

num(100)

