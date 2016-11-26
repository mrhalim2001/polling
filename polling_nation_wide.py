import random

#simulate 2016 America in the memory of a machine
blue_voters = 64223986
red_voters = 62206395
america = ['Blue']*blue_voters+['Red']*red_voters
winning_color = 'Blue' if blue_voters>red_voters else 'Red'

#try polls of increasing sizes
for size_of_poll in [10, 50, 100, 500, 1000, 5000, 10000]:

	#for every poll size, simulate a poll of that size over and over, a million times
	number_of_simulations = 1000000
	score_card = []
	for i in range(0, number_of_simulations):
		poll = random.sample(america, size_of_poll)
		blue_polled_voters = sum([x=='Blue' for x in poll])
		red_polled_voters = sum([x=='Red' for x in poll])
		predicted_winner = 'Blue' if blue_polled_voters>red_polled_voters else 'Red'
		prediction_is_correct = (winning_color == predicted_winner)
		score_card += [prediction_is_correct]
		
	#keep tabs on how often a poll of this size lead to the wrong prediction
	probability_error = int(100.0 * (1.0 - sum(score_card)/float(number_of_simulations)))

	print("Polling "+str(size_of_poll)+" random voters led to the wrong prediction "
	+str(probability_error)+"% of the time" )
		
#the mark of a true data scientist is to include a coin flip 
#in every probabilistic comparison as a sanity check
number_of_simulations = 1000000
score_card = []
for i in range(0, number_of_simulations):
		predicted_winner = 'Blue' if random.random()>0.5 else 'Red'
		prediction_is_correct = (winning_color == predicted_winner)
		score_card += [prediction_is_correct]
probability_error = int(100.0 * (1.0 - sum(score_card)/float(number_of_simulations)))
print("Flipping a coin led to the wrong prediction "+str(probability_error)+"% of the time" )

