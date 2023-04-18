from cryptogram_helper import *
from english_words import get_english_words_set
import time

# CHECK RESULTS WITH https://www.boxentriq.com/code-breaking/cryptogram

cryptogram = "CFBCTF VKF YOYVTTE OABMQFS XAFW PAFE SDOMBUFK D'J WBP V UFKE MBJCFPFWP FTFMPKDMDVW"


# Tools
version = '0.01'
start = time.time() # Grab Currrent Time Before Running the Code
web2lowerset = get_english_words_set(['web2'], lower=True)
GCIDElowerset = get_english_words_set(['gcide'], lower=True)
end = time.time() # Grab Currrent Time After Running the Code
set_time = end - start # Subtract Start Time from The End Time

# Choose the word set
all_english_words = GCIDElowerset

all_english_words.add('usually')
all_english_words.add('shocked')

# Create the necesary lists of candidate words
crypto_list = cryptogram.split()
candidate_dict = {}

start = time.time() # Grab Currrent Time Before Running the Code
for this_word in crypto_list:
    word_format = check_word_format(this_word)
    possible_candidates = []
    for possible_candidate in all_english_words:
        candidate_word_format = check_word_format(possible_candidate)
        if candidate_word_format == word_format:
            possible_candidates.append(possible_candidate.upper())
    candidate_dict[this_word] = possible_candidates
end = time.time() # Grab Currrent Time After Running the Code
candidate_list_time = end - start # Subtract Start Time from The End Time

solved_cryptogram = ''
mini_dict = {}
old_mini_dict = mini_dict.copy()
prefix = "  \ "

start = time.time() # Grab Currrent Time Before Running the Code
solve_cryptogram_recursive(crypto_list, mini_dict, solved_cryptogram, candidate_dict, prefix)
end = time.time() # Grab Currrent Time After Running the Code
total_time = end - start # Subtract Start Time from The End Time
print("Total time of generating words set:", str(set_time))
print("Total time of generating candidate list:", str(candidate_list_time))
print("Total time of solving cryptogram:", str(total_time))