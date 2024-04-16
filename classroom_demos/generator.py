def multiples_of_five(n):
    for i in range(n):
        yield i * 5


# Example usage
result = list(multiples_of_five(10))
print(result)
