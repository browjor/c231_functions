import math
import operator
import re
import string
from primefac import primefac
from prettytable import PrettyTable

lowercase_letter_set = set()
for lowercase in string.ascii_lowercase:
    lowercase_letter_set.add(lowercase)

top_english_set = set()
top_english_set.add('a')
top_english_set.add('e')
top_english_set.add('o')
top_english_set.add('i')


alpha_to_position_dict = {}
for i in range(97,123):
    alpha_to_position_dict[chr(i)] = i-96

r_shift_to_keyword_char_dict = {}
j = 0
for i in range(97,123):
    r_shift_to_keyword_char_dict[j] = chr(i)
    j += 1

position_to_alpha_dict = {}
for i in range(97,123):
    position_to_alpha_dict[i-96] = chr(i)


def load_IC_R_FrequencyTable_into_dict(dict):
    result = make_frequency_tables(dict["String"])
    dict["Table"] = result[0]
    dict["Exact IC"] = result[1]
    dict["Approx IC"] = result[2]
    dict["Approx R"] = result[3]


def print_Sequence_and_FactorList(stringy,  range_int_or_tuple,  repeat=2, is_tuple=False):
    '''given text, a keyword length, an iteration range (start,stop), and minimum number of
    repeating occurrences, default and lower range 2'''
    if is_tuple:
        for i in range(range_int_or_tuple[0], range_int_or_tuple[1]+1):
            print(f"Repeating sequences of {i} characters in text.")
            sequence = find_repeating_sequences(stringy, i, repeat)
            print(sequence)
            factor_set = find_positions_of_repeating_sequences_and_factoring(stringy, sequence)
            print(f"Common prime factors of differences in position between {i} sized repeating sequences.")
            print(factor_set)
            print("\n")
    else:
        print(f"Repeating sequences of {range_int_or_tuple} characters in text.")
        sequence = find_repeating_sequences(stringy, range_int_or_tuple, repeat)
        print(sequence)
        factor_set = find_positions_of_repeating_sequences_and_factoring(stringy, sequence)
        print(f"Common prime factors of differences in position between {range_int_or_tuple} sized repeating sequences.")
        print(factor_set)
        print("\n")

def print_IC_R_of_loaded_dict(dict, name):
    print(f"Name of text: {name}\nExact IC: {dict['Exact IC']}\n"
          f"Approx IC: {dict['Approx IC']}\nApprox R: {dict['Approx R']}\n")

def split_strings_print_IC_for_keyword_size(stringy, range_int_or_tuple, is_tuple=False):
    if is_tuple:
        for i in range(range_int_or_tuple[0], range_int_or_tuple[1] + 1):
            print(f"Splitting text into {i} columns.")
            split = split_string_into_columns(stringy, i)
            average_IC = 0
            print("Analysis of letter distribution in each column:")
            for j in range(1, i + 1):
                temp_result = make_frequency_tables(split[j])
                average_IC += temp_result[1]
            print(f"Average IC for a keyword size of {i} is {average_IC/i}.")

    else:
        print(f"Splitting text into {range_int_or_tuple} columns.")
        split = split_string_into_columns(stringy, range_int_or_tuple)
        average_IC = 0
        for j in range(1, range_int_or_tuple + 1):
            temp_result = make_frequency_tables(split[j])
            average_IC += temp_result[1]
        print(f"Average IC for a keyword size of {range_int_or_tuple} is {average_IC/range_int_or_tuple}.")

def split_strings_find_shift_Es_solve_cipher(stringy, keyword_size):
    #split string into r blocks, with each string in a dict numbered according to position mod keyword size
    split = split_string_into_columns(stringy, keyword_size)
    pre_combine_dict = {}
    r_shifts_list = []
    # for each block string, put the count of letters into a list with their count, and sort the list with reverse=True (descending)
    for block in split:
        block_letter_count = {}
        for alpha in lowercase_letter_set:
            block_letter_count[alpha] = 0
            for lettery in split[block]:
                if lettery == alpha:
                    block_letter_count[alpha] += 1
        frequency_list = sorted(block_letter_count.items(), key=operator.itemgetter(1), reverse=True)
        top_letters = []
        for i in range(5):
            top_letters.append(frequency_list[i][0])
        # go into letter logic for each of the top five letters
        r_shift = evaluate_top_choices_return_highest_shift(top_letters)
        r_shifts_list.append(r_shift)
        new_string = ""
        #shift each block string
        for block_letter in split[block]:
            c_position = alpha_to_position_dict[block_letter]
            p_position = (c_position - r_shift) % 26
            if p_position == 0:
                p_position += 26
            new_string += position_to_alpha_dict[p_position]
        #put it all back together
        pre_combine_dict[block] = new_string

    plaintext = join_string_from_blocks(pre_combine_dict, stringy)
    keyword = ""
    for i in range(keyword_size):
        shift = r_shifts_list[i]%26
        if shift < 0:
            shift += 26
        keyword += r_shift_to_keyword_char_dict[shift]
    return plaintext, keyword



def evaluate_top_choices_return_highest_shift(top_letter_choice_list):
    # if the shift for the most frequent letter to 'e' makes the second highest frequency 't, a, o, or i' then give it plus 1
    # if the shift makes the third highest frequency 't, a, o, or i', then give it plus 1, and so on for the other 4 letters in the top 5 most frequent letters
    # sort the rating and choose the one with the highest score
    potential_shifts = []
    #e = 5
    e_position = alpha_to_position_dict['e']
    for i in range(5):
        #r = c - p
        r_shift = alpha_to_position_dict[top_letter_choice_list[i]]-e_position
        score = 0
        #for other letters than the shifted e
        for j in range(5):
            if j == i:
                continue
            else:
                c_position = alpha_to_position_dict[top_letter_choice_list[j]]
                #p = c - r
                p_position = (c_position-r_shift)%26
                if p_position == 0:
                    p_position += 26
                #if p is a, o , i, t
                if position_to_alpha_dict[p_position] in top_english_set:
                    score += 1
        potential_shifts.append((r_shift, score))
    #sort for and return best scoring shift
    potential_shifts.sort(key=operator.itemgetter(1), reverse=True)
    return potential_shifts[0][0]


def split_strings_to_columns_print_frequencies(stringy, range_int_or_tuple, is_tuple=False):
    if is_tuple:
        for i in range(range_int_or_tuple[0],range_int_or_tuple[1]+1):
            print(f"Splitting text into {i} columns.")
            split = split_string_into_columns(stringy, i)
            print(split)
            print()
            print("Analysis of letter distribution in each column:")
            for j in range(1,i+1):
                temp_result = make_frequency_tables(split[j])
                title = f"Size {i} Keyword, Column {j}"
                print_string_prettytable(temp_result[0], title)

    else:
        print(f"Splitting text into {range_int_or_tuple} columns.")
        split = split_string_into_columns(stringy, range_int_or_tuple)
        print(split)
        print()
        print("Analysis of letter distribution in each column:")
        for j in range(1, range_int_or_tuple + 1):
            temp_result = make_frequency_tables(split[j])
            title = f"Size {range_int_or_tuple} Keyword, Column {j}"
            print_string_prettytable(temp_result[0], title)

def find_missing_alphabet_letters(string, dict_name):
    letter_set = set()
    for letter in string:
        letter_set.add(letter)
    #print out the missing letters with a set difference
    if len(letter_set) != 26:
        print(dict_name)
        print(f"Some letters are missing from string {dict_name}")
        missing_letter_set = lowercase_letter_set.difference(letter_set)
        for missing_letter in missing_letter_set:
            print(missing_letter)


# takes list of lists, display for each letter [letter - count - relative frequency - percentage], returns list of tables
#dict format is list_dict = {"Processed Plaintext": {"String Ident": Z , "Exact IC": a , "Approx IC": b , "Approx R": c , "Table" : d }}
def make_frequency_tables(string):
    indiv_table = PrettyTable()
    indiv_table.field_names = ["Letter", "Count", "RelativeFrequency", "Percentage"]
    #calculating IC on the go
    exact_IC_sum = 0
    approx_IC_sum = 0
    approx_r = 0
    num_letters = len(string)
    #for character in the alphabet
    for alpha in lowercase_letter_set:
        count = 0
        #get the count of that character in the string
        for lettery in string:
            if lettery == alpha:
                count += 1
        indiv_table.add_row([alpha,count,f"{(count/num_letters):10.4f}",f"{(100*count/num_letters):10.4f}"])
        #calculating IC
        exact_IC_sum += (count * (count - 1)) / (num_letters * (num_letters -1))
        approx_IC_sum += (math.pow(count/num_letters,2))
        approx_r = (0.027*num_letters) / ((exact_IC_sum * (num_letters - 1)) - (0.038 * num_letters) + 0.065)

    return indiv_table, exact_IC_sum, approx_IC_sum, approx_r

#printing my lovely tables
def print_dict_prettytable(dict, name):
    #want to sort by the count, can be changed
    print(f"Table of Letter Frequency for {name}")
    print(dict["Table"].get_string(sort_key=operator.itemgetter(2), reversesort=True, sortby="Count"))
    print("\n")

def print_string_prettytable(string_table, name):
    print(name)
    print(string_table.get_string(sort_key=operator.itemgetter(2), reversesort=True, sortby="Count"))
#getting occurrences of words together

#kasiski analysis
#plan is to make a huge list of the letters except do a smarter thing, use regex
#going to start with 3 keywords and work up, when no matching sequences are found, the search quits
#for a 406 size string, the bounds are 0,405 for indexing and with a size 3 keyword that means 403 is the last index. so upper bound - r + 1 is the highest index
#if there is at least 2 matches of a sequence, it is added along with its count
#the count is squared if i do absolutely nothing, 1 match means no value like it, 2 matches means 4 total, 3 matches 9 total.
#I'll know something is wrong if the counts aren't squared, and ill take the root for the true value at the end
#with a match comes the position, but i'll handle that after

#pass in string
def find_repeating_sequences(string, keyword_size, minimum_repeats_allowed):
    pattern_set = {}
    final_index = len(string) - 1
    start_index = 0
    end_index = start_index + keyword_size
    starting_piece = string[start_index:end_index]
    while end_index <= final_index:
        starting_piece = string[start_index:end_index]
        matches = re.findall(starting_piece, string)
    #very inefficient but hey cryptography takes time, right?
        for match in matches:
            if match in pattern_set:
                pattern_set[match] +=1
            else:
                pattern_set[match]=1
        start_index += 1
        end_index += 1
    new_dict_set = {}
    # because of the code, the number of occurrences of the same string is squared
    minimum_repeats_allowed -= 1
    minimum_repeats_allowed *= minimum_repeats_allowed
    for fragment in pattern_set:
        if pattern_set[fragment] > minimum_repeats_allowed:
            new_dict_set[fragment] = math.sqrt(pattern_set[fragment])
    return new_dict_set


def find_positions_of_repeating_sequences_and_factoring(string, dict_set):
    # going through string, finding positions of repeating occurrences
    repeated_fragment = {}
    factor_dict = {}
    for fragment in dict_set:
        repeated_fragment[fragment] = []
        matchy = re.search(fragment, string)
        offset = 0
        while matchy:
            repeated_fragment[fragment].append((matchy.start() + offset, matchy.end() + offset))
            offset += matchy.end()
            matchy = re.search(fragment, string[offset + 1:])

    #calculating differences between the positions of occurrences, factoring them down to primes, and returning them
    for fragment in repeated_fragment:
        pre_factor_list = []
        for i in range(1,len(repeated_fragment[fragment])):
            pre_factor_list.append(int(repeated_fragment[fragment][i][0])-int(repeated_fragment[fragment][i-1][0]))
        for difference in pre_factor_list:
            prime_list = list(primefac(difference))
            for prime in prime_list:
                if prime in factor_dict:
                    factor_dict[prime] += 1
                else:
                    factor_dict[prime] = 1
    new_dict = {}
    for fragment in factor_dict:
        if factor_dict[fragment] > 1:
            new_dict[fragment] = factor_dict[fragment]
    #return a list of factors for comparison
    sorted_factor_dict = dict(sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_factor_dict


def split_string_into_columns(string, key_size):
    string_dict = {}
    for i in range(1, key_size+1):
        string_dict[i] = ""
    for i in range(0, len(string)):
        if (i+1)%key_size == 0:
            string_dict[key_size] += string[i]
        else:
            string_dict[(i+1)%key_size] += string[i]
    return string_dict

def join_string_from_blocks(string_dict, original_text):
    combined_string = ""
    #might need this if index wants to go too far
    #empty_block_count = 0
    for i in range(0, len(original_text)):
        if (i+1)%len(string_dict) == 0:
            combined_string += string_dict[len(string_dict)][0]
            string_dict[len(string_dict)]=string_dict[len(string_dict)][1:]
        else:
            combined_string += string_dict[(i+1)%len(string_dict)][0]
            string_dict[(i+1)%len(string_dict)] = string_dict[(i+1)%len(string_dict)][1:]
    if len(combined_string) != len(original_text):
        print("WARNING!!!!!!! LENGTH OF COMBINED STRING IS NOT EQUAL TO ORIGINAL STRING!!!!!!!")
    return combined_string






