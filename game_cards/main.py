from CardGame_class import *

print("**War Cards Game**")
print("=======================")

# Initialize new card game requesting for the players names
card_game=CardGame(input("Enter Player 1 name: "),input("Enter Player 2 name: "))
player1=card_game.player1
player2=card_game.player2
# Print player1 and player2 details
print(card_game)
print("=======================")
# 10 rounds game.
rounds=1
while rounds<11:
    # Pick cards from the players every round check which one has bigger value
    card1=player1.get_card()
    card2=player2.get_card()
    # The player who won the round take both cards
    if card1>card2:
        print(player1.name,f"won round {rounds}:",card1, ">", card2)
        player1.add_card(card1)
        player1.add_card(card2)
    else:
        print(player2.name,f"won round {rounds}:",card1, "<", card2)
        player2.add_card(card2)
        player2.add_card(card1)
    rounds+=1

print("=======================")
# Print the quantity of cards in deck left for each player
print(f"{player1.name} left with {len(player1.player_deck)} cards.")
print(f"{player2.name} left with {len(player2.player_deck)} cards.")

# Check the result with get winner function and print the winner name if there is one.
if card_game.get_winner() is None:
    print("The result is draw")
else:
    print("THE WINNER IS:",card_game.get_winner().name,"!!!!\nHis cards deck after the game:",card_game.get_winner().player_deck)