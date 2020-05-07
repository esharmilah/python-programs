test_str = input()
res_first = test_str[0:len(test_str)//2] 
res_second = test_str[len(test_str)//2 if len(test_str)%2 == 0
                                 else ((len(test_str)//2)+1):] 
a=res_first[::-1]
b=res_second[::-1]
print(a+b)
