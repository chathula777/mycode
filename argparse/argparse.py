#!/usr/bin/python3

"""enter an adjective describing me"""

import argparse

#this will hold all the arguments
parser_mcgee = argparse.ArgumentParser(description="Describe Chathula in one word")

#acceptable values
acc_adj = ["awesome", "good", "stunning", "intelligent"]

#add some arguments
parser_mcgee.add_argument("adj", choices=acc_adj, help = "This word describe Chathula")

#add an optional arguement
parser_mcgee.add_arguement("-a", metavar="ADVERB", default="so", help="'Helper words, like 'really,very,exciting',etc.")

#have the parser obj turn all those arguemtns in to variables

arglebargle = parser_mcgee.parse_args()

print(f"Chathula is {arglebargle.a} {arglebargle.adj}!")



