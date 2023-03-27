for n in range(2, 101):
    num1 = 3 + 2*n + n**2
    num2 = 3 + 9*(n+2)
    if num1 == num2:
        print(n)
        break
# proverka, esli 2 <= n <= 32.
print(int("123", 9), int("93", 11))