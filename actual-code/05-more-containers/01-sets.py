empty_set = set()

print(empty_set)
print(type(empty_set))

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print(len(basket))
print('apple' in basket)

for item in basket:
    print(item)

basket.add('apricot')
basket.add('apricot')
basket.add('apricot')

print(basket)

basket.remove('apricot')
if 'apricot' in basket:
    basket.remove('apricot')
print(basket)

