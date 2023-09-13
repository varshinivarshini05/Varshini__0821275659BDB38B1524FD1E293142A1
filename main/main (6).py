#- Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object. 

# define the base class player
class Player:
   def play(self):
     print("The Player Is Playing Cricket")

# define the derived class batsman
class Batsman(Player):
  def Play(self):
    print("The Batsman Is Batting")

# define the derived class bowler
class Bowler(Player):
  def Play(self):
    print("The Bowler Is Bowling")

# create an object for Batsman and Bowler
batsman = Batsman()
bowler = Bowler()

# call the play method for each object
batsman . Play()
bowler . Play()
