#rock paper scissors
import random
list_of_possibilities = ["rock","paper","scissors"]

dict_of_win_or_lose = {
   ("rock","paper"): "win of computer",
   ("rock","scissors"): "win of player",
   ("rock","rock"): "Tie",
   ("paper","rock"): "win of player",
   ("paper","paper"): "Tie",
   ("paper","scissors"): "win of computer",
   ("scissors","rock"): "win of computer",
   ("scissors","paper"): "win of player",
   ("scissors","scissors"): "Tie"
   }

counters = {
    "paper":"scissors",
    "scissors":"rock",
    "rock":"paper"
    
    
    }

pp, pr, ps = 0, 0, 0

win_counter = 0
lose_counter = 0
tie_counter = 0

def comp_move():
    ###This part should keep your moves from games and identify most popular and use counter move
    if ps == pp == pr:
        return counters[random.choice(list_of_possibilities)]
    elif ps == pr and pp < pr:
        return counters[random.choice(["scissors","rock"])]
            
    elif pr == pp and ps < pr:
        return counters[random.choice(["rock","paper"])]
    
    elif ps == pp and pr < pp:
        return counters[random.choice(["scissors","paper"])]
    else:
        stats = {"paper": pp, "rock": pr, "scissors": ps}
        most_popular = max(stats, key=stats.get)
        return counters[most_popular]
        
def pre_gameplay():
    while True:
        
        gameplay(comp_move())
        
    
    
def gameplay(move_from_comp):
    global pp, pr, ps, win_counter, lose_counter, tie_counter
    game_list = ()
    while True:
        selection = input("Rock, Paper or Scissors: ").lower()
        if selection not in list_of_possibilities:
            print("Please write one thing from the choice: Rock, Paper or Scissors")
        else:
            break
    comp_choice = move_from_comp
    if selection == "paper":
        pp+=1
    elif selection == "rock":
        pr+=1
    else:
        ps+=1
    krutoi_tuple = tuple((selection,comp_choice))
    print(f"Computer choiced: {comp_choice}")
    print(dict_of_win_or_lose[krutoi_tuple])
    if dict_of_win_or_lose[krutoi_tuple] == 'win of player':
        win_counter +=1
    elif dict_of_win_or_lose[krutoi_tuple] == 'win of computer':
        lose_counter +=1
    else:
        tie_counter +=1
    print(f"Wins: {win_counter}, Loses: {lose_counter}, Ties: {tie_counter}")
            
    
    
pre_gameplay()
