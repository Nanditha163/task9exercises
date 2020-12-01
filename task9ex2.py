def fibonacci(count):
    fiblist=[0,1]
    any(map(lambda _:fiblist.append(sum(fiblist[-2:])),range(2,count)))
    return fiblist[:count]
print(fibonacci(10))


OUTPUT:
C:\Users\Dell\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/Dell/PycharmProjects/pythonProject/task9ex2.py
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
