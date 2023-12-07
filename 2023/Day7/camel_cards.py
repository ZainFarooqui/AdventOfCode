file_path = 'example.txt'
data = []
mapping_table = str.maketrans({'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'})
with open(file_path, 'r') as file:
	
	for line in file:
		data.append(line.strip().translate(mapping_table))
  
count = len(data)

hand_bid_map = {}

for el in data:
    hand, bid = el.split(" ")
    hand_bid_map[hand] = bid

types = {
	(5): [],
	(4, 1): [],
	(3, 2): [],
	(3, 1 ,1): [],
	(2, 2, 1): [],
	(2, 1, 1, 1): [],
	(1, 1, 1, 1, 1): []
}

card_counts = {}
for hand in hand_bid_map.keys():
	card_count = {}
	for card in hand:
		if card not in card_count:
			card_count[card] = 0
		card_count[card] += 1
	card_counts[hand] = card_count
	hand_type = tuple(sorted(card_count.values(), reverse=True))
	print(hand_type)
	types[hand_type].append(hand)

print(types)


