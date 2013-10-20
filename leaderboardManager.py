#!/usr/bin/env python

from time import sleep
from time import time
import string
from parse_rest.connection import register
from parse_rest.datatypes import Object

class PlayerStats(Object):
  pass
  
class LeaderboardObject(Object):
  pass

if __name__ == '__main__':
   while 1:
     field = ('veryEasy', 'veryEasyPerfect', 
              'easy', 'easyPerfect', 
              'medium', 'mediumPerfect',
              'hard', 'hardPerfect',
              'insane', 'insanePerfect',
              'numAchievements')
     category = ('Very Easy:', 'Very Easy Perfect', 
                 'Easy', 'Easy Perfect', 
                 'Medium', 'Medium Perfect',
                 'Hard', 'Hard Perfect',
                 'Insane', 'Insane Perfect',
                 'Num Achievements')
       
     register('keys redacted')
     leaderboardString = ""
     #print time()
     #Query Db For All Player Stats
     allStats = PlayerStats.Query.all()
     print 'Query done.'
     #Go through each field, and construct ranking
     for i in range(1, len(field)):
        print 'Building stats for ', category[i], '.\n';
        leaderboardString += (category[i] + '\n')
        currentRankings = allStats.order_by('-' + field[i])
        rank = 1
        for playerStat in currentRankings:
          if playerStat.name:
            leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.__dict__[field[i]]) + '\n')
          rank += 1
          if rank > 5:
            break
     print leaderboardString, "\n\n"
     print 'Querying for current board'
     Delete current leaderBoard, should only be one, but use for loop just in case
     currentBoards = LeaderboardObject.Query.all()
     for board in currentBoards:
       board.delete()
     Create new leaderboard with the stats just generated
     leaderboardObject = LeaderboardObject(string = leaderboardString, time = str(time()))
     leaderboardObject.save()
     print 'done'
     sleep(30)

