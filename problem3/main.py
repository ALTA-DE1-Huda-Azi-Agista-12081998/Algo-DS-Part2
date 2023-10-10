def playing_domino(cards, deck):
    suggested_cards = []

    for card in cards:
        if deck[0] in card or deck[1] in card:
            suggested_cards.append(card)

    if suggested_cards:
        return max(suggested_cards, key=sum)
    else:
        return []

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []