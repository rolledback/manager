#!/user/bin/env python

from random import randrange
from time import sleep
from time import time
from Queue import Queue
from threading import Thread
import string, random
from parse_rest.connection import register
from parse_rest.datatypes import Object

class Worker(Thread):
  def __init__(self, tasks):
    Thread.__init__(self)
    self._id = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
    self.tasks = tasks
    self.daemon = True
    self.start()
  
  def run(self):
    while True:
      print 'I looking for a function! ' + str(self._id)
      func, args, kargs = self.tasks.get(True, None)
      try:
        print 'I gots me a function! ' +  str(self._id)
        func(*args, **kargs)
      except Exception, e:
        print 'Worker exception:'
        print e
      finally:
        self.tasks.task_done()

class PlayerStats(Object):
  pass
  
class LeaderboardObject(Object):
  pass
  
class ThreadPool:
  def __init__(self, numThreads):
    self.tasks = Queue(numThreads)
    for _ in range(numThreads): Worker(self.tasks)
    
  def addTask(self, func, *args, **kargs):
    self.tasks.put((func, args, kargs))

  def waitCompletion(self):
    self.tasks.join()
    
class LeaderboardManager(Thread):
  def waitDelay(self, d):
    print 'sleeeeping'
    sleep(d)
    
  def generateLeaderboard(self):
    register('43b1wG09syjYsstMxzNNFAYA2xRQ7EHSZLnNt34z', '0hd57bxJOijeDn6r4iMxwxJ3jSK3McXJI9hcjqL2')
    leaderboardString = ''
    print '\n--------------------------\ngo'
    print time()
    try:
      #Query Db For All Player Stats
      allStats = PlayerStats.Query.all()   
      print 'Query done'
      #These need to be divided and conquered, get on it
      print 'Very Easy'
      #Very Easy      
      leaderboardString += ('Very Easy' + '\n')
      currentRanking = allStats.order_by('-veryEasy')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.veryEasy) + '\n')
          rank += 1
        if rank > 5:
          break
      print 'Very Easy Perfect'
      #Very Easy Perfect	
      leaderboardString += ('Very Easy Perfect' + '\n')
      currentRanking = allStats.order_by('-veryEasyPerfect')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.veryEasyPerfect) + '\n')
          rank += 1
        if rank > 5:
          break
      print 'Easy'
      #Easy	  
      leaderboardString += ('Easy' + '\n')
      currentRanking = allStats.order_by('-easy')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.easy) + '\n')
          rank += 1
        if rank > 5:
          break  
      print 'Easy Perfect'
      #Easy Perfect
      leaderboardString += ('Easy Perfect' + '\n')
      currentRanking = allStats.order_by('-easyPerfect')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.easyPerfect) + '\n')
          rank += 1
        if rank > 5:
          break
      print 'Medium'
      #Medium
      leaderboardString += ('Medium' + '\n')
      currentRanking = allStats.order_by('-medium')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.medium) + '\n')
          rank += 1
        if rank > 5:
          break
      print 'Medium Perfect'
      #Medium Perfect
      leaderboardString += ('Medium Perfect' + '\n')
      currentRanking = allStats.order_by('-mediumPerfect')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.mediumPerfect) + '\n')
          rank += 1
        if rank > 5:
          break
      print 'Hard'
      #Hard
      leaderboardString += ('Hard' + '\n')
      currentRanking = allStats.order_by('-hard')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.hard) + '\n')
          rank += 1
        if rank > 5:
          break
      print 'Hard Perfect'
      #Hard Perfect
      leaderboardString += ('Hard Perfect' + '\n')
      currentRanking = allStats.order_by('-hardPerfect')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.hardPerfect) + '\n')
          rank += 1
        if rank > 5:
          break
      print 'Insane'
      #Insane
      leaderboardString += ('Insane' + '\n')
      currentRanking = allStats.order_by('-insane')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.insane) + '\n')
          rank += 1
        if rank > 5:
          break
      print 'Insane Perfect'
      #Insane Perfect
      leaderboardString += ('Insane Perfect' + '\n')
      currentRanking = allStats.order_by('-insanePerfect')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.insanePerfect) + '\n')
          rank += 1
        if rank > 5:
          break
      print 'Num Achievements'
      #Number of Achievements
      leaderboardString += ('Num Achievements' + '\n')
      currentRanking = allStats.order_by('-numAchievements')
      rank = 1
      for playerStat in currentRanking:
        if playerStat.name:
          leaderboardString += (str(rank) + '. ' + playerStat.name + ' ' + str(playerStat.numAchievements) + '\n')
          rank += 1
        if rank > 5:
          break

    except Exception, e:
      print 'Function exception'
      print e
    finally:
      print 'Querying for current board'
      #Delete current leaderBoard, should only be one, but use for loop just in case
      currentBoards = LeaderboardObject.Query.all()
      for board in currentBoards:
        board.delete()
      #Create new leaderboard with the stats just generated
      leaderboardObject = LeaderboardObject(string = leaderboardString, time = str(time()))
      leaderboardObject.save()
      print 'done'
      print time()

  def activityMetrics():
    return
    
  def gameMetrics():
    return
    
  def __init__(self):
    Thread.__init__(self)
    self.pool = ThreadPool(3)
    self.running = True
  
  def run(self):
    while self.running:
      print self.pool.tasks.qsize()
      self.pool.addTask(self.generateLeaderboard)
      #self.pool.addTask(self.waitDelay, 5)
      sleep(60)
  
  def stop(self):
    self.pool.tasks.join()
    self.join()
    
if __name__ == '__main__':
  manager = LeaderboardManager()
  manager.run()
