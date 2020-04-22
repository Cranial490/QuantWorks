import positionManager as pm
positions = {}
pm.update_positions(positions, 'A', 5, 10, 'BUY')
pm.update_positions(positions, 'A', 7, 10, 'BUY')
pm.update_positions(positions, 'A', 9, 10, 'BUY')
# update_positions(positions, 'RIL', 17, 100, 'SELL')
# update_positions(positions, 'ADANI', 15, 50, 'SELL')
pm.update_positions(positions, 'A', 6, 50, 'SELL')


print(positions)
