import sys
import random

rcards = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
CARDS = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_hand = []
dealer_hand = []

def draw_card():
	return(random.choice(CARDS))

def running_total(ucards):
	return sum(ucards)

def calculate_winner(user_score, dealer_score):
	print(f'Your cards: {user_hand} = {user_score}')
	print(f'Dealer cards: {dealer_hand} = {dealer_score}')
	
	if(user_score > 21 or (dealer_score<21 and dealer_score>user_score)):
		print('You lose!')
	elif(dealer_score > 21 or (user_score<21 and user_score>dealer_score)):
		print('You win!')
	else:
		print('Tie game')

def end_game(user_score, dealer_score):
	calculate_winner(user_score, dealer_score)
	rematch = input('Press \'y\' to play again, or \'n\' to quit\n')
	if rematch.lower() == 'y':
		user_hand = dealer_hand = []
		play_game()
	else:
		sys.exit(0)

def play_game():
	print('-- Welcome to BlackJack --\n')

	for x in range(2):
		user_hand.append(draw_card())
	dealer_hand.append(draw_card())
	covered_card = draw_card()

	print(f'Your cards: {user_hand}')
	print(f'Dealer\'s first card: {dealer_hand}')
	dealer_hand.append(covered_card)

	while(True):
		u_score = running_total(user_hand)
		d_score = running_total(dealer_hand)
		if(u_score > 21 or d_score > 21):
			end_game(u_score, d_score)
		
		resp = input('Press \'y\' to draw again, or \'n\' to pass\n')
		if(resp.lower() == 'n'):
			end_game(u_score, d_score)
		else:
			user_hand.append(draw_card())
			print(user_hand)

play_game()