def World_Cup():

  print("Your in the world Cup final, you are England against Spain, you are currently 1-0 down.")
  print("you have the ball")
  print("Do You pass it the")
  print("A.left wing")
  print("B.right wing")
  decision = input("Decision: ")

  if decision.lower() == "a":
        left_wing()

  if decision.lower() == "b":
        right_wing()

def left_wing():

    print("You recieve the ball on the left wing")
    print("Do you")
    print("a.Dribble down the wing and cross into the box")
    print("b.Take it into the middle")
    decision = input("Decision: ")

    if decision.lower() == "a":
        box()

    if decision.lower() == "b":
        print("you are fouled, but the ref blows his full time whistle! Spain are the champs! You lose!")
        print("Restarting...")
        print("")
        World_Cup()
        
def right_wing():

    print("The ball is passed to the right wing")
    print("Do you")
    print("a.Dribble down the wing and cross into the box")
    print("b.pass it to the keeper")
    decision = input("Decision: ")

    if decision.lower() == "a":
        box()

    if decision.lower() == "b":
        keeper()



def box():

   print("The ball has been crossed into the box")
   print("Do you")
   print("a.head it at goal")
   print("b.head it to you Vardy on the edge of the box")
   decision = input("Decision: ")

   if decision.lower() == "a":
     print("Straight into the keepers arms, the whistle blows it's full time you lose")
     print("Restarting...")
     print("")
     World_Cup()

   if decision.lower() == "b":
        ("Vardy strikes it, back off the net, it's full time and it's 1-1, penalties it is")
        penalties()



   
   

    

    
    

    
     
    

    







# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    World_Cup()
