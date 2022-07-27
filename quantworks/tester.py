import positionManager as pm
import util
positions = {}
pm.place_order(positions, 'A', 5, 10, 'BUY')
pm.place_order(positions, 'A', 6, 30, 'SELL')
# pm.place_order(positions, 'A', 4, 40, 'SELL')
# pm.place_order(positions, 'A', 3, 60, 'BUY')


print(positions)
