def print_number_diamond(n):
  
    for i in range(1, n + 1):
        print(" " * (n - i) + " ".join(str(j) for j in range(1, i + 1)))

    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + " ".join(str(j) for j in range(1, i + 1)))


n = int(input("Enter the size of the diamond: "))
print_number_diamond(n)
