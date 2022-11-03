import random

def get_choices():

  player_choice = input('Enter a choice (Rock, Paper, Scissors, I Quit): ')
  options = ['rock', 'paper', 'scissors, I quit']
  computer_choice = random.choice(options)
  choices = {'player': player_choice, 'computer': computer_choice}
  return choices

def check_win(player, computer):
    while True:
      print(f"You chose {player}, computer choice {computer}. ")
      if player == 'I Quit'.lower():
       print("Thank you for playing")
       break
      if player == computer:    
        return "it's a tie"
      elif player == 'Rock'.lower():
        if computer == "Scissors".lower():
          return "rock smashes scissors, you wins!"  
        else:
           return "paper covers rock, you loose." 
      elif player == 'Paper'.lower():
         if computer == "Rock".lower():
            return "paper covers rock! you win"  
         else:
             return "scissors cuts paper, you loose." 
      elif player == 'Scissors'.lower():
        if computer == "Paper".lower():
            return "scissors cuts paper, you wins!"  
        else:
           return "rock smashes scissors, you loose."
      else:
        print("invalid input")
        break


choices = get_choices()
result = check_win(choices["player"],choices["computer"])

print(result)