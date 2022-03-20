import os

print('Welcome to the secret Auction')
bids = {}
more_bids = True


while more_bids:
    name = input('What is your name?\n> ')
    bid = int(input('What is your bid?\n> '))
    more_bidders = input('Are there any other bidders? yes | no\n> ').lower()
    if more_bidders != 'yes':
        more_bids = False

    bids[name] = bid

    if more_bidders == 'no':
        winning_bid = max(bids.values())
        
        for person in bids:
            if bids[person] == winning_bid:
                winning_bidder =  person




print(f'The winning bidder is: {winning_bidder} with a winning bid of: {winning_bid}!')