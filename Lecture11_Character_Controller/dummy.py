table = {
    'SLEEP' : {'Hit' : 'WAKE'},
    'WAKE' : {'TIMER10' : 'SLEEP'}
}

cur_state = 'SLEEP'
event = 'HIT'
next_state = table[cur_state][event]
print(table[cur_state]['Hit'])
print(table['WAKE']['TIMER10'])