import random
import csv

#read 2016 ballot count per state from data file
#source: http://uselectionatlas.org/RESULTS/
states = {}
with open('vote count by state.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			state_name = row[0]
			states[state_name] = {}
			states[state_name]['weight'] = int(row[1])
			states[state_name]['blue_voters'] = int(row[2].replace(",", ""))
			states[state_name]['red_voters'] = int(row[3].replace(",", ""))
			states[state_name]['total_voters'] = states[state_name]['blue_voters'] + states[state_name]['red_voters']

#simulate 2016 America (state by state) in the memory of a machine
total_voters = 126752509
total_electoral_count = []
for state in states:
	states[state]['voters'] = ['B']*states[state]['blue_voters']+['R']*states[state]['red_voters']
 	states[state]['winning_color'] = 'B' if states[state]['blue_voters']>states[state]['red_voters'] else 'R'
	total_electoral_count += [states[state]['winning_color']]*states[state]['weight']
winning_color = 'B' if total_electoral_count.count('B') > total_electoral_count.count('R') else 'R'

#try polls of increasing sizes
for size_of_poll in [25000, 50000, 100000]: #[100, 500, 1000, 5000, 7500, 10000]:

	#for every poll size, simulate a poll of that size over and over, a million times
	number_of_simulations = 1000000
	score_card = []
	for i in range(0, number_of_simulations):
	
		polling_ratio =  float(size_of_poll) / float(total_voters) 
		predicted_electoral_count = []
		national_poll_count = 0
		for state in states:
			poll_count_per_state = int(states[state]['total_voters']*polling_ratio)+1
			national_poll_count += poll_count_per_state
			poll = random.sample(states[state]['voters'], poll_count_per_state)
			blue_polled_voters = sum([x=='B' for x in poll])
			red_polled_voters = sum([x=='R' for x in poll])
			predicted_state_winner = 'B' if blue_polled_voters>red_polled_voters else 'R' if blue_polled_voters<red_polled_voters else 'N'
			predicted_electoral_count += [predicted_state_winner]*states[state]['weight']
		predicted_national_winner = 'B' if predicted_electoral_count.count('B') > predicted_electoral_count.count('R') else 'R' if predicted_electoral_count.count('B') < predicted_electoral_count.count('R') else 'N'
		prediction_is_correct = (winning_color == predicted_national_winner)
		score_card += [prediction_is_correct]
					
	#keep tabs on how often a poll of this size lead to the wrong prediction
	probability_error = int(100.0 * (1.0 - sum(score_card)/float(number_of_simulations)))
	
	print("Polling "+str(size_of_poll)+" random voters led to the wrong prediction "+str(probability_error)+"% of the time" )


#the mark of a true data scientist is to include a coin flip 
#in every probabilistic comparison as a sanity check
number_of_simulations = 1000000
score_card = []
for i in range(0, number_of_simulations):

	polling_ratio =  float(size_of_poll) / float(total_voters) 
	predicted_electoral_count = []
	national_poll_count = 0
	for state in states:
		poll_count_per_state = int(states[state]['total_voters']*polling_ratio)+1
		national_poll_count += poll_count_per_state
		predicted_state_winner = 'B' if random.random()>0.5 else 'R'
		predicted_electoral_count += [predicted_state_winner]*states[state]['weight']
	predicted_national_winner = 'B' if predicted_electoral_count.count('B') > predicted_electoral_count.count('R') else 'R' if predicted_electoral_count.count('B') < predicted_electoral_count.count('R') else 'N'
	prediction_is_correct = (winning_color == predicted_national_winner)
	score_card += [prediction_is_correct]
probability_error = int(100.0 * (1.0 - sum(score_card)/float(number_of_simulations)))
print("Flipping a coin led to the wrong prediction "+str(probability_error)+"% of the time" )


	
	
