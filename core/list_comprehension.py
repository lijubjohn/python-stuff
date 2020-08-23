
# new_list = [expression for member in iterable]
squares = [i * i for i in range(10)]

TAX_RATE = .08


def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
final_prices = [get_price_with_tax(i) for i in txns]
print(final_prices)


# new_list = [expression for member in iterable (if conditional)]
sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)


# new_list = [expression (if conditional) for member in iterable]

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)


# in sets
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)


# in dictionaries
squares = {i: i * i for i in range(10)}
print(squares)