australia_blacklist = {'Joe', 'Marta', 'Peter', 'Anna', 'Julia'}
poker_blacklist = {'Peter', 'Mark', 'Anna', 'John', 'Olha', 'Marta'}
alcohol_blacklist = {'Julia', 'Anna', 'Peter', 'Vadim', 'Oleh'}

print('Jackpot winners: ', ', '.join(australia_blacklist.intersection(poker_blacklist, alcohol_blacklist)))
