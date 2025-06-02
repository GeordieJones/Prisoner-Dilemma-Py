# True means to share
# False means Take

def peacefulStrat(opponentMove):
    return True

def angryStrat(opponentMove):
    return False

def Tit_for_tat(opponentMove):
    if opponentMove == None:
        return True
    else:
        return opponentMove
    

tat_track = 0
def Tit_for_2tats(opponentMove):
    global tat_track
    if opponentMove == False:
        tat_track += 1
        if tat_track < 2:
            return True
        return False
    tat_track = 0
    return True