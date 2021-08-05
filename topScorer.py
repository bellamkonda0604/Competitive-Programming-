# topScorer(data) [10 Points]
# Write the function topScorer(data) that takes a multi-line 
# string encoding scores as csv data for some kind of 
# competition with players receiving scores, so each 
# line has comma-separated values. The first value on 
# each line is the name of the player (which you can 
# assume has no integers in it), and each value after 
# that is an individual score (which you can assume is a 
# non-negative integer). You should add all the scores 
# for that player, and then return the player with the 
# highest total score. If there is a tie, return all the 
# tied players in a comma-separated string with the names 
# in the same order they appeared in the original data. 
# If nobody wins (there is no data), return None (not the 
# string "None"). So, for example:

def topScorer(data):
    # Your code goes here...
    if data == '':
        return None
    return bestplayer(data)

def bestplayer(data):
    name = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = 0
    player = ''
    for line in data.splitlines():
        currentscore = 0
        currentname = ''
        for i in line.split(','):
            if i[0] in name or i[0] in name.lower():
                currentname = i
            else:
                currentscore += int(i)
            if currentscore > score:
                score = currentscore
                player = currentname
            elif currentscore == score:
                if currentname not in player:
                    player += "," + currentname
    return player


data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
assert(topScorer(data) == 'Fred')

data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
assert(topScorer(data) == 'Wilma')

data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
assert(topScorer(data) == 'Fred,Wilma')

assert(topScorer('') == None)
print("All test cases passed...!")
# Hint: you may want to use both splitlines() and split(',') here!
