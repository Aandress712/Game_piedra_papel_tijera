import random

def choos_options():
    options = ('piedra', 'papel' , 'tijera')
    user_option = input("Debes escoger entre: Piedra, Papel o Tijera => ")
    user_option = user_option.lower()
    
    if not user_option in options:
        print("Esta no es una opcion apropiada para este juego")
        return None, None
    
    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  
  if user_option == computer_option:
      print("¡Empate!")
  elif user_option == "piedra":
      if computer_option == "tijera":
          print("Piedra gana a Tijera")
          print("User Win")
          user_wins += 1
      else:
          print("Papel gana a Piedra")
          print("Computer Win")
          computer_wins += 1
  elif user_option == "papel":
      if computer_option == "piedra":
          print ("Papel gana a Piedra")
          print("User Win")
          user_wins += 1
      else:
          print("Tijera gana a Papel")
          print("Computer Win")
          computer_wins += 1
  elif user_option == "tijera":
      if computer_option == "papel":
          print("Tijera gana a Papel")
          print("User Win")
          user_wins += 1
      else:
          print("Piedra gana a Tijera")
          print("Computer Win")   
          computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  ganador = False
  while ganador==False:
      print("*" * 10)
      print("ROUND", rounds)
      print("*" * 10)
      
      print('computer_wins', computer_wins)
      print('user_wins' , user_wins)
      rounds += 1

      user_option, computer_option = choos_options()
      user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)


      if user_wins == 2:
          print("Congratulations you win")
          ganador=True
      
      if computer_wins ==2:
          print("Sorry the computer win you")
          ganador=True

run_game()