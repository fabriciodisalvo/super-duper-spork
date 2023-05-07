from cryptogram_helper import *

# Version
version = '0.01' # First draft
version = '0.02' # Solve words in order of possible candidates, then re-sort
version = '0.03' # Work on generating candidate out of grand list.
# CHECK RESULTS WITH https://www.boxentriq.com/code-breaking/cryptogram
cryptogram = "CFBCTF VKF YOYVTTE OABMQFS XAFW PAFE SDOMBUFK D'J WBP V UFKE MBJCFPFWP FTFMPKDMDVW"

# Create the necesary lists of English words
start = time.time() # Grab Currrent Time Before Running the Code
all_english_words = get_english_words_set(['gcide'], lower=True) # Choose the word set
all_english_words.add('usually') # Update the word set
all_english_words.add('shocked') # Update the word set
end = time.time() # Grab Currrent Time After Running the Code
set_time = end - start # Subtract Start Time from The End Time

# Generate candidate list
start = time.time() # Grab Currrent Time Before Running the Code
crypto_list = cryptogram.split()
candidate_dict = {}
candidate_dict = generate_candidate_list(crypto_list, all_english_words, candidate_dict)
end = time.time() # Grab Currrent Time After Running the Code
candidate_list_time = end - start # Subtract Start Time from The End Time

# Solve cryptogram
start = time.time() # Grab Currrent Time Before Running the Code
tuple_list = [] # Order cryptogram by less candidates
for i in candidate_dict:
    tuple_list.append((len(candidate_dict[i]), i))
tuple_list.sort()
new_crypto_list = [x[1] for x in tuple_list]
order_dict = {} # Create order reference
for x in range(len(crypto_list)):
    for i in range(len(tuple_list)):
        if tuple_list[i][1] == crypto_list[x]:
            order_dict[x] = i
solved_cryptogram = ''
mini_dict = {}
print("The New York Times cryptogram solver, version", version)
solve_cryptogram_recursive(new_crypto_list, mini_dict, solved_cryptogram, candidate_dict, order_dict)
end = time.time() # Grab Currrent Time After Running the Code
total_time = end - start # Subtract Start Time from The End Time

# End + Log
# print("Total time of generating words set:", str(set_time))
# print("Total time of generating candidate list:", str(candidate_list_time))
# print("Total time of solving program:", str(total_time))
# print("Total time of full solving cryptogram:", str(set_time + candidate_list_time + total_time))
# print()