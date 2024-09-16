import csv, difflib, re

'''
    For UWM Math 98/108 Instructors:

    This script will take a Math 98 and a Math 108 Gradebook and merge them into a new gradebook
    that can be directly uploaded to Canvas. Simply copy the two gradebook csv files into the Gradebooks
    folder and modify the GB_98 and GB_108 variables to match the names of your csv files. You may
    then run the script.
    
    Once the script has been run, the command console will display all Math 98/108 assignments that 
    were copied into the new gradebook along with the new grades. Please ensure to double check that the list of assignments
    appears correct. 
    
    If something doesn't look right, please contact Stephen Lasinis at slasinis@uwm.edu
'''

GB_98 = 'Gradebooks\\98_09_14_2024.csv'
GB_108 = 'Gradebooks\\108_09_14_2024.csv'

gb_108 = []
gb_98 = []
gb_new_98 = []

with open(f'{GB_98}', 'r') as f:
    for r in csv.reader(f):
        gb_98.append(r)
        gb_new_98.append(r.copy())
with open(f'{GB_108}', 'r') as f:
    for r in csv.reader(f):
        gb_108.append(r)

col_map = {}
for c in range(len(gb_108[0])):
    col_map[gb_108[0][c][0: len(gb_108[0][c])-10]] = c

# for k, v in col_map.items():
#     print(f'{k}: {v}')

for c in range(6, len(gb_98[0])-4):
    s: str = gb_98[0][c][0: len(gb_98[0][c])-10]
    bm = difflib.get_close_matches(s, col_map.keys())
    if len(bm) == 0 or s[0] == 'A' or re.sub(r'\D', '', bm[0]) == '108':
        continue
    col = col_map[bm[0]]
    if not gb_108[2][col] == '':
        print(bm[0])
        for r in range(2, len(gb_98)):
            gb_new_98[r][c] = gb_108[r][col]
            print(f'{gb_new_98[r][0]} => {gb_new_98[r][c]}')
        print()

with open(f'Gradebooks\\new_98_gradebook.csv', 'w', newline='') as f:
    csv.writer(f).writerows(gb_new_98)