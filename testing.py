for n in range(2, 101):
    num1 = 4 + 5*n + n**2
    num2 = int("35", 9)
    num3 = 7*(n + 1) + pow(n+1, 2)
    if num1 + num2 == num3:
        print(n)
# proverka, esli 2 <= n <= 32
print(int("154", 7) + int("35", 9), int("170", 8))