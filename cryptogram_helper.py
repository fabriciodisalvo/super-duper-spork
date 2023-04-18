from english_words import get_english_words_set
import time

# Tools


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def generate_candidate_list(crypto_list, all_english_words, candidate_dict):
    for this_word in crypto_list:
        word_format = check_word_format(this_word)
        possible_candidates = []
        for possible_candidate in all_english_words:
            if len(possible_candidate) == len(this_word):
                candidate_word_format = check_word_format(possible_candidate)
                if candidate_word_format == word_format:
                    possible_candidates.append(possible_candidate.upper())
        candidate_dict[this_word] = possible_candidates
    return candidate_dict


def check_word_format(word):
    available_letters = letters.copy()
    word_format = ""
    dict_letters = {}
    for letter in word:
        if letter in dict_letters:
            word_format = word_format + dict_letters[letter]
        else:
            dict_letters[letter] = available_letters.pop(0)
            word_format = word_format + dict_letters[letter]
    return(word_format)


def solve_cryptogram_recursive(cr_list, min_dict, solved_crgram, cand_dict, order_solved_crgram):
    if cr_list == []:
        solved_phrase = ''
        solved_crgram_list = solved_crgram.split()
        for position in range(len(solved_crgram_list)):
            position_word = solved_crgram_list[order_solved_crgram[position]]
            solved_phrase = solved_phrase + position_word + ' '
        print()
        print(solved_phrase)
        print()
        return True
    else:
        word_to_decrypt = cr_list[0]
        next_candidate_dict = cand_dict.copy()
        # Candidates review
        for candidate in next_candidate_dict[word_to_decrypt]:
            next_min_dict = min_dict.copy()
            # Update mini-dict
            test_against_previous_candidate = True
            for letter_to_check in range(len(word_to_decrypt)):
                if word_to_decrypt[letter_to_check] in next_min_dict:
                    if next_min_dict[word_to_decrypt[letter_to_check]] == candidate[letter_to_check]:
                        continue
                    else:
                        test_against_previous_candidate = False
                        break
            if test_against_previous_candidate:
                for letter_to_check in range(len(word_to_decrypt)):
                    next_min_dict[word_to_decrypt[letter_to_check]] = candidate[letter_to_check]
            else:
                continue
            next_solved_crgram = solved_crgram + ' ' + candidate
            next_cr_list = cr_list[1:]
            if solve_cryptogram_recursive(next_cr_list, next_min_dict, next_solved_crgram, next_candidate_dict, order_solved_crgram):
                return True
            # else:
            #     print("So far, this is what we have:", solved_crgram)
