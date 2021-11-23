from aocutils import get_raw

def get_input():
    player1, player2 = get_raw(22).split('\n\n')
    deck1 = [int(card) for card in player1.splitlines()[1:]]
    deck2 = [int(card) for card in player2.splitlines()[1:]]
    return deck1, deck2

def problem1():
    deck1, deck2 = get_input()
    while len(deck1) > 0 and len(deck2) > 0:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    winner = deck1 if len(deck1) > 0 else deck2
    return sum([winner[i] * (len(winner) - i) for i in range(len(winner))])

def problem2():
    deck1, deck2 = get_input()
    player1_wins = recursive_combat(deck1, deck2)
    winner = deck1 if player1_wins else deck2
    return sum([winner[i] * (len(winner) - i) for i in range(len(winner))])

def recursive_combat(deck1, deck2):
    played = set()
    while len(deck1) > 0 and len(deck2) > 0:
        if (tuple(deck1), tuple(deck2)) in played:
            return True
        played.add((tuple(deck1), tuple(deck2)))
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 <= len(deck1) and card2 <= len(deck2):
            player1_wins = recursive_combat(deck1[:card1], deck2[:card2])
        else:
            player1_wins = card1 > card2
        if player1_wins:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    return len(deck2) == 0