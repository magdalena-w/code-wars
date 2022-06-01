def square_sum(numbers):
    result = []
    for n in numbers:
        result.append(pow(n, 2))
    return sum(result)