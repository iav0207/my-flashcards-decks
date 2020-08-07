import csv
import re


def parse_cards(string):
    card_strings = string.split('### Card ')[1:]
    cards = []
    for cs in card_strings:
        slices = re.split(r'\n+', cs)
        cards.append({
            'num': slices[0],
            'front': slices[2][2:],
            'back': slices[4][2:],
            'side': slices[5][2:] if len(slices) > 5 else '',
        })
    return cards


def main():
    with open('resources/decks.csv') as infile:
        reader = csv.reader(infile)
        decks = []
        for row in reader:
            if 'coverImage' in row:
                continue
            decks.append({
                'name': row[0],
                'description': row[1],
                'content': row[3],
            })
    for deck in decks:
        cards = parse_cards(deck['content'])
        with open(f'out/{deck["name"].replace(":", "").replace(" ", "_").replace(".", "")}.csv', 'w') as outfile:
            writer = csv.writer(outfile)
            keys = ['num', 'front', 'back', 'side']
            writer.writerow(keys)
            writer.writerows([[c[k] for k in keys] for c in cards])


if __name__ == '__main__':
    main()
