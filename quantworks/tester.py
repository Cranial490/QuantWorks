import positionManager as pm
import util
positions = {}
pm.place_order(positions, 'A', 5, 10, 'BUY')
# pm.update_positions(positions, 'A', 7, 10, 'BUY')
# pm.update_positions(positions, 'A', 9, 10, 'BUY')
# update_positions(positions, 'RIL', 17, 100, 'SELL')
# update_positions(positions, 'ADANI', 15, 50, 'SELL')
pm.place_order(positions, 'A', 6, 30, 'SELL')
pm.place_order(positions, 'A', 4, 40, 'SELL')
pm.place_order(positions, 'A',3,60,'BUY')


print(positions)
