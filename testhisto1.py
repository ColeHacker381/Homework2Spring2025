from homework2 import histogram

data = [-2, -2.2, 0, 5.6, 8.3, 10.1, 30, 4.4, 1.9, -3.3, 9, 8]
input_dictionary = {'data': data, 'n': 15, 'min_val': -5, 'max_val': 10}
hist = histogram(input_dictionary)
print(hist)
