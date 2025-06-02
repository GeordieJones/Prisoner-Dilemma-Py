from random import randint
import prisonerStrategies

TOTAL_GAMES = 5

player1_points = 0
player2_points = 0

player1_lastmove = None
player2_lastmove = None

# player1 strategy = import your second strategy
player1 = prisonerStrategies.Tit_for_2tats
# player2 strategy = import your second strategy
player2 = prisonerStrategies.angryStrat

def runGame(player1Choice, player2Choice):
    global player1_points, player2_points, player1_lastmove, player2_lastmove
    
    player1_lastmove = player1Choice
    player2_lastmove = player2Choice

    if player1Choice == player2Choice:
        player1_points += 3
        player2_points += 3
    elif player1Choice != player2Choice:
        if not player1Choice:
            player1_points += 5
        else:
            player2_points +=5
    else:
        player1_points += 1
        player2_points += 1

def simulation():
    global player1_points, player2_points, player1_lastmove, player2_lastmove
    for games in range(TOTAL_GAMES):
        ROUNDS = randint(195, 210)
        for rounds in range(ROUNDS):
            runGame(player1(player2_lastmove), player2(player1_lastmove))
        print(f'GAME {games}:'
            f'---------total rounds played: {ROUNDS} ---------\n'
            f'player1 points: {player1_points} \n'
            f'player2 points: {player2_points}'
            )
        player1_points = 0
        player2_points = 0
        player1_lastmove = None
        player2_lastmove = None
        
simulation()

