import os

clear = lambda: os.system('cls')

from art import logo

print(logo)


# bidding = []
# def add_bids(name, bid):
#     bidding.append(
#         {key : value}
#     )

# biddingloop = True
# while biddingloop:
#     key = input("What is your name?: ")
#     value = int(input("What's your bid?: "))
#     add_bids(key,value)
#     anotherbidder = input("Are there any other bidders? Type 'yes' or 'no': ")
#     if anotherbidder == "no":
#         biddingloop = False
#     else:
#         clear()

# print(bidding)

# #bidding = [{'san': 2}, {'kate': 5},{'san1': 1}, {'kate1': 3}]
# newbidding = {}
# for item in bidding:
#     newbidding.update(item)

# print(newbidding)

# y = {k: v for k, v in sorted(newbidding.items(), key=lambda item: item[1], reverse=True)}
# print(y)

# print("The Winner is", list(y.keys())[0], "with a bid of $", list(y.values())[0])

def bidderreport(bid):
    highest_bid = 0
    for item in bid:
        bid_amount = bid[item]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = item
    print(f"The winner is {winner}, with a bid of ${highest_bid}")


bids = {}
biddingloop = True
while biddingloop:
    key = input("What is your name?: ")
    value = int(input("What's your bid?: "))
    bids[key] = value
    anotherbidder = input("Are there any other bidders? Type 'yes' or 'no': ")
    if anotherbidder == "no":
        biddingloop = False
        print(bids)
        bidderreport(bids)
    else:
        clear()
