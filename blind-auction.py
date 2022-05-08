print('''
                        Welcome to the blind auction software.
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\ ''')

auction_state = True

bidders_dict = {}

def greatest_bidder(bidders):
    values_list = list(bidders.values())
    keys_list = list(bidders.keys())

    index_max_value = values_list.index(max(values_list))
    max_key = keys_list[index_max_value]

    print(f"The winner of the bid is {max_key} with a bid of {values_list[index_max_value]}")

while auction_state != False:    
    bidder_name = input("Enter the bidder's name: ")
    bidder_bid = int(input("Enter your bid: "))

    bidders_dict[bidder_name] = bidder_bid

    continue_bid = input("Are there any more bidders: (Y/N) ").lower()

    if continue_bid == "n":
        auction_state = False

# print(bidders)

greatest_bidder(bidders_dict)