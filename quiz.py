
score = 0
name = ""

def quiz():
    global name

    print("The Ultimate Football Quiz")
    print("To play just input the letter you think the answer is")
  
    name = input("Name: ")
    question1()
    question2()
    question3()
    end()

def question1():
    global score
    global name
    
    print("Question 1")
    print("who is the youngest player on the current England senior national squad?")
    print("A","Marcus Rashford")
    print("B","Alex Oxlade Chamberlain")
    print("C","Chris Smalling")
    Answer = input("Answer, ")

    if Answer.lower() == "a":
          score = score + 1
          print("Correct!")

    else:
          print("Incorrect!")
          
   

def question2():
    global score
    global name
    
    print("Question 2")
    print("Who is englands all time top scorer?")
    print("A","Gary Lineker")
    print("B","Wayne Rooney")
    print("C","Bobby Charlton")
    Answer = input("Answer, ")

    if Answer.lower() == "b":
          score = score + 1
          print("Correct!")
          
    else:
        print("Incorrect!")

def question3():
    global score
    global name
    
    print("Question 3")
    print("Who is Englands most capped player?")
    print("A","Steven Gerrard")
    print("B","David Beckham")
    print("C","Peter Shilton")
    Answer = input("Answer, ")

          
    if Answer.lower() == "c":
          score = score + 1
          print("Correct!")
    else:
        print("Incorrect!")

def end():
    global score
    global name
    
    print("Your score is",score)

    if score == 0:
        print(name,"Your a nutter")

    if score == 1:
        print("You did OK",name)

    if score == 2:
        print("You did decent",name)

    if score == 3:
        print(name,"You're a genious")
              






# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
