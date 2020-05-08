from quantworks import positionManager as pm
from quantworks import util
positions = {}


pm.place_order(positions, 'A', 10, 10, 'SELL')
print(positions)
pm.place_order(positions, 'A', 12, 5, 'BUY')
print(positions)
pm.place_order(positions, 'A', 15, 7, 'BUY')
print(positions)

''' Tc 2
pm.place_order(positions, 'A', 10, 10, 'BUY')
print(positions)
pm.place_order(positions, 'A', 12, 5, 'SELL')
print(positions)
pm.place_order(positions, 'A', 15, 7, 'SELL')
print(positions)

pm.place_order(positions, 'A', 18, 2, 'BUY')
print(positions)
pm.place_order(positions, 'A', 16, 10, 'SELL')
print(positions)
pm.place_order(positions, 'A', 14, 5, 'BUY')
print(positions)
pm.place_order(positions, 'A', 15, 10, 'BUY')
print(positions)
#pm.place_order(positions, 'A', 16, 10, 'BUY')
#print(positions)
pm.place_order(positions, 'A', 17, 5, 'SELL')
print(positions)
'''


''' Tc 3
pm.place_order(positions, 'A', 10, 10, 'SELL')
print(positions)
pm.place_order(positions, 'A', 12, 10, 'SELL')
print(positions)
pm.place_order(positions, 'A', 15, 15, 'SELL')
print(positions)
pm.place_order(positions, 'A', 12, 6, 'BUY')
print(positions)
pm.place_order(positions, 'A', 8, 20, 'BUY')
print(positions)
pm.place_order(positions, 'A', 17, 10, 'BUY')
print(positions)
'''

# Tc4
# pm.place_order(positions, 'A', 10, 10, 'SELL')
# print(positions['A'])
# pm.place_order(positions, 'B', 10, 10, 'BUY')
# print(positions['B'])
# pm.place_order(positions, 'A', 12, 5, 'BUY')
# print(positions['A'])
# pm.place_order(positions, 'B', 12, 5, 'SELL')
# print(positions['B'])
# pm.place_order(positions, 'A', 15, 7, 'BUY')
# print(positions['A'])
# pm.place_order(positions, 'B', 15, 7, 'SELL')
# print(positions['B'])
# print(positions)


