#define the base player
class player:
  def play(self):
    print("the player is playing cricket.")

#define the derived class bastman
class batsman(player):
  def play(self):
    print("the batsman is batting.")

#define the derived class bowler
class bowler(player):
  def play(self):
    print("the bowler is bowling.")

#create object of batsman and bowler class
batsman = batsman()
bowler = bowler()

#call the play()method for each object
batsman.play()
bowler.play()
