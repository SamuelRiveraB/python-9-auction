
quit = False
bidders = {}

print("Welcome to the Secret Auction Program")
while (quit == False):
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bidders[name] = bid
    more_bidders = input("Any more bidders? yes / no\n").lower()
    if more_bidders == "no":
        max = 0
        winner = ''
        for key in bidders:
            if(bidders[key] > max):
                max = bidders[key]
                winner = key
        print(f"Max bidder: {winner} with {max}")
        quit = True