class Player:
    def __init__(self,money,name):
        self.money = money
        self.name = name
    def call(self,imbalance):
        self.money -= imbalance
        global imba = 0
        global currentmoney += imbalance
        print("{} make a call".format(self.name))
    def rais(self,moneyraise):
        self.money -= moneyraise
        global imba = moneyraise - global imba
        global currentmoney += moneyraise
        print("{} make a raise of {}".format(self.name,moneyraise))
    def check(self):
        print("{} check".format(self.name))
    def fold(self,enemy,currentmoney):
        print("{} fold".format(self.name))
        enemy.win(currentmoney)
        raise Gameover
    def win(self,currentmoney):
        self.money += currentmoney
        print("{} wins".format(self.name)))
        raise Gameover
    def even(self,currentmoney,enemy):
        self.money += currentmoney/2
        enemy.money += currentmoney/2
        print ("Even game")
        raise Gameover
def bargin(imba,currentmoney,ai,me):
    ai.cal(imba,currentmoney)
        while True:
           a = Input("1.call 2.fold 3.raise 4.check")
           if a ==1:
             me.call(imba)
             break
           elif a==2:
             me.fold(ai,currentmoney)
             break
           elif a==3:
             me.rais(input("money raise\n"))
             break
           elif a==4:
             me.check()
             break
    while imba !=0:
        ai.cal(imba,currentmoney)
        if imba ==0:
            break
        while True:
           a = Input("1.call 2.fold 3.raise 4.check")
           if a ==1:
             me.call(imba)
             break
           elif a==2:
             me.fold(ai,currentmoney)
             break
           elif a==3:
             me.rais(input("money raise\n"))
             break
           elif a==4:
             me.check()
             break
            
print ("Game Start!")
ai = Player(500,"Deep Green")
me = Player(500,"Me")
while ai.money>0 and me.money>0:
  try:
    while True:
      lib = [21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124,131,132,133,134,141,142,143,144]
      pick = sample(lib,9)
      ai.money-=1
      me.money-=2
      imba = 1
      currentmoney = 3
      print(pick[0], pick[1])
      bargin(imba,currentmoney,ai,me)
      print(pick[0],pick[1],pick[2],pick[3],pick[4])
      bargin(imba,currentmoney,ai,me)
      print(pick[0],pick[1],pick[2],pick[3],pick[4],pick[5])
      bargin(imba,currentmoney,ai,me)
      print(pick[0],pick[1],pick[2],pick[3],pick[4],pick[5],pick[6])
      bargin(imba,currentmoney,ai,me)
      print(pick[0],pick[1],pick[2],pick[3],pick[4],pick[5],pick[6],pick[7],pick[8])
      mepick = [pick[0],pick[1],pick[2],pick[3],pick[4],pick[5]]
      aipick = [pick[2],pick[3],pick[4],pick[5],pick[6],pick[7],pick[8]]
      if compare.convert(aipick)>compare.convert(mepick):
        ai.win(currentmoney)
      elif compare.convert(aipick)>compare.convert(mepick):
        me.win(currentmoney)
      else:
        ai.even(currentmoney,me)
  except Gameover:
      pass
        
    
    
    
        
        
