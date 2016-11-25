
spain = 1
england = 0


def World_Cup():
  global spain
  global england

  print("")
  print("")
  print("WORLD CUP GAME 2018!!!!!")
  print("Your in the world Cup final, you are England against Spain, you are currently 1-0 down.")
  print("you have the ball")
  import time
  time.sleep(1)
  print("Do You pass it the")
  print("A.left wing")
  print("B.right wing")
  decision = input("Decision: ")

  if decision.lower() == "a":
        left_wing()

  if decision.lower() == "b":
        right_wing()

def left_wing():
    global spain
    global england

    print("")
    print("")
    print("You recieve the ball on the left wing")
    import time
    time.sleep(1)
    print("Do you")
    print("a.Dribble down the wing and cross into the box")
    print("b.Take it into the middle")
    print("c.pass it down the wing to the edge of the box")
    decision = input("Decision: ")

    if decision.lower() == "a":
        box()

    if decision.lower() == "b": 
        print("you are fouled, but the ref blows his full time whistle!","Spain",spain,"-",england,"England")
        print("Restarting...")
        import time
        time.sleep(5)
        World_Cup()

    if decision.lower() == "c":
        print("It goes down to the side of the box and then its passed to the edge of the box")
        vardy()
        
def right_wing():
    global spain
    global england

    print("")
    print("")
    print("The ball is passed to the right wing")
    import time
    time.sleep(1)
    print("Do you")
    print("a.Dribble down the wing and cross into the box")
    print("b.pass it to the keeper")
    decision = input("Decision: ")

    if decision.lower() == "a":
        box()

    if decision.lower() == "b":
        keeper()



def box():
   global spain
   global england

   print("")
   print("")
   print("The ball has been crossed into the box")
   import time
   time.sleep(1)
   print("Do you")
   print("a.head it at goal")
   print("b.head it to you the edge of the box")
   decision = input("Decision: ")

   if decision.lower() == "a":

     print("")
     print("") 
     print("Straight into the keepers arms, the full time whistle blows","Spain",spain,"-",england,"England")
     print("Restarting...")
     import time
     time.sleep(5)
     World_Cup()

   if decision.lower() == "b":
        print("It is headed to the edge of the box")
        vardy()



   
def keeper():
  global spain
  global england


  print("")
  print("")
  print("It is passed to the keeper but, he keeps it too long, the full time whistle blows","Spain",spain,"-",england,"England")
  print("Restarting...")
  import time
  time.sleep(5)
  World_Cup()

def vardy():
  global spain
  global england


  print("")
  print("")
  print("Vardy recieves it on the edge of the box")
  import time
  time.sleep(1)
  print("Do you")
  print("a.Strike it top left corner")
  print("b. hit it in the middle")
  decision = input("Decision: ")

  if decision.lower() == "a":
        england = england + 1
        print("He shoots! He scores","Spain",spain,"-",england,"England")
        penalties()

  if decision.lower() == "b":
        print("the keeper pushes the ball over the bar, Corner!")
        corner()

def corner():
  global spain
  global england

  print("")
  print("")  
  print("Walcott crosses the ball in")
  import time
  time.sleep(1)
  print("Do you")
  print("a.Go over for an over head kick")
  print("b.Try to keep it simple and go for a header")
  decision = input("Decision: ")


  if decision.lower() == "a":
        england = england + 1
        print("The over head kick works, He scores","Spain",spain,"-",england,"England")
        penalties2()

  if decision.lower() == "b":
        print("You miss and the full time whistle blows","Spain",spain,"-",england,"England")
        print("Restarting...")
        import time
        time.sleep(5)
        World_Cup()








def penalties():
  global spain
  global england
  
  print("")
  print("")
  print("It has come down to penalties, it is 5-5,sudden death, next goal is winner!")
  import time
  time.sleep(1)
  print("Do you")
  print("a.Strike it down the middle")
  print("b.Hit it top left corner")
  print("c.kick it bottom right corner")
  decision = input("Decision: ")

  if decision.lower() == "a" or decision.lower() == "c":
    print("You lose! Spain are champs!")
    print("Restarting...")
    import time
    time.sleep(5)
    World_Cup()

  if decision.lower() == "b":
    print("What a goal!, England are the champions of the world!!!!!!!")
    print("Restarting...")
    import time
    time.sleep(5)
    World_Cup()


def penalties2():
  global spain
  global england
  
  print("")
  print("")
  print("It has come down to penalties, it is 5-5,sudden death, next goal is winner!")
  import time
  time.sleep(1)
  print("Do you")
  print("a.Strike it down the middle")
  print("b.Hit it top left corner")
  print("c.kick it bottom right corner")
  decision = input("Decision: ")


  if decision.lower() == "b" or decision.lower() == "c":
    print("You lose! Spain are champs!")
    print("Restarting...")
    import time
    time.sleep(5)
    World_Cup()

  if decision.lower() == "a":
    print("What a goal!, England are the champions of the world!!!!!!!")
    print("Restarting...")
    import time
    time.sleep(5)
    World_Cup()
    

   

    



# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    World_Cup()
