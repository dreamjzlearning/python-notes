# 10.3.py
# try-expect

a = 1
b = 0
try:
    ans = a / b
except ZeroDivisionError:  # 捕获到异常
    print("cannot divide by zero")
else:  # try 部分正常执行
    print(ans)
