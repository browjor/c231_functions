from useful_c231.kasiski_and_IC import *
from string_manip.preprocessing import *

def full_week1_ass2():
    original_text = """Looking for repeating substrings can be tedious, and if the cipher is monoalphabetic, then the Kasiski test doesn't help us any. How can we tell from the start whether or not one or more alphabets are being used?

    The idea here is that the frequency table of an MSC should look like the one for standard English, just with the letters matching different frequencies. The way we actually go about measuring this is a little different from this, but it gets at the same thing. We use the Index of Coincidence."""

    preprocessed_original = remove_space_and_punctuation(original_text)

    problem_3a_string = """rsoborgwuvrvviakorgjafskxmnxygaehitvjmolyenuojtykgignirzyqoeuelgnebvzmckninknikrymsboxejzhovyrtykpplyenpnswtgrwvzilclvodzlejzerkcleknirfxrokurefxqoikelgnebvzwaikfeztkujkhtykmdvgleikmsknetknifikuuvtgykgflvujaeswcjnsucjpofqpibkxhvurewuvskgrdrxheempijnnujzaiknxhvritkkvsdgxcyorguojfvxinklvehaintoiskniwreaerixurrpyxuebfaxmvgwuiorgknmszyelzzxlvjmfwkveezjrfsxhzyfukoxgvzwakzlejgqeknmnxciujkxhvordvdsftumntoheeii"""
    problem_3b_string = """svvrpunmvyylwlhapunzbizaypunzjhuilalkpvbzhukpmaoljpwolypztvuvhswohilapjaoluaolrhzpzrpalzakvlzuaolswbzhufovdjhudlalssmyvtaolzahyadolaolyvyuvavulvytvylhswohilazhylilpunbzlkaolpklholylpzaohaaolmylxblujfahislvmhutzjzovbsksvvrsprlaolvulmvyzahukhyklunspzoqbzadpaoaolslaalyzthajopunkpmmlyluamylxblujplzaoldhfdlhjabhssfnvhivbatlhzbypunaopzpzhspaaslkpmmlyluamyvtaopzibapanlazhaaolzhtlaopundlbzlaolpuklevmjvpujpklujl"""
    problem_3c_string = """ncazcgkwqfdtjxekkbshouwktwzvmveedsftxbsluozscyxygquebxvzuaacitpgjontnbgkjszibxoruwezcmijvratmgxygzbjmtrpjcirugavvsxazksdvvqhntvkyvqibxvftbaiigiftaagytpgjontnleigpqxhzyjgrfwybhvcvqgybwkjofibxjigegthvckcpxtiyeeogohbhycfzadeembghttigiwqfeiughrtrqcaemjjxghnpmkjhttfxxkgfebumgykbsscyjvtszizkihwszrcxwkjsipspirehgpfecxqondomqvcgggcgkkjwexmtpzvhxtxbjwgfqcnyvfohtxmuykkhstnlekvvqhufikjwzvqxyjghttcghvzcrribrtkrqcwx"""

    problem_4_string = """qwjozsoasiwmkiryqikjzjnxinvbwtfvwikjldslxiihzkbcitnxciinahsetigtyfjzxzhbcieypzorxqnozymnxutmnrkmmgtlxiicytexeebmoicqnmsdypzwkfzoayjbciitzisktvzsirwmirqxcesjbneijjzmelcniuypzmujiciijqnxyfbolvkzzuljvxckfjgifkiiqjhacslqlgsfptdovypzsejnjvjyiihrwlzrxqqnlazaoazypolvqmoxvwahekhpdrxiqajvwmixwwmlyvskdijypzardezetycvpcdojestcoqvfapvzsoolzxqnecnbopviqajvwmixwwwhxynawyknbbikxioxyjavqvypdrxbmpwvypzmeimsswhwdrtnlzrtj"""

    # make sure preprocessing is right
    has_equal_string_lengths = True

    list_names = ["Processed Plaintext", "Problem 3a", "Problem 3b", "Problem 3c", "Problem 4"]
    # dict format is list_dict = {"Processed Plaintext": {"Exact IC": a , "Approx IC": b , "Approx R": c , "Table" : d }}
    list_dict = {}
    for list_name in list_names:
        list_dict[list_name] = {"Name": list_name, "String": "", "Exact IC": 0.00, "Approx IC": 0.00, "Approx R": 0.00,
                                "Table": PrettyTable, "DictSet": {}, "FactorList": set()}
    list_dict["Processed Plaintext"]["String"] = preprocessed_original
    list_dict["Problem 3a"]["String"] = problem_3a_string
    list_dict["Problem 3b"]["String"] = problem_3b_string
    list_dict["Problem 3c"]["String"] = problem_3c_string
    list_dict["Problem 4"]["String"] = problem_4_string

    # make sure all 26 letters are there


    if (len(preprocessed_original) != len(problem_3a_string) or
            len(preprocessed_original) != len(problem_3b_string) or
            len(preprocessed_original) != len(problem_3c_string) or
            len(preprocessed_original) != len(problem_4_string)):
        print("text length not correct")
        has_equal_string_lengths = False
        exit()
    else:
        print(f"Number of letters in original text is {len(preprocessed_original)} and matches the ciphers.")

    if not has_equal_string_lengths:
            print("warning, string lengths are messed up")

    print("\n")
    print("Checking that all letters from the alphabet are present in both the plaintext and for problem 3.a, 3.b, and 3.c.")

    print("\n")

    for dict in list_dict:
        find_missing_alphabet_letters(list_dict[dict]["String"], dict)

    print("Answering question 3:")
    print("\n")

    for dict in list_dict:
        result = make_frequency_tables(list_dict[dict]["String"])
        list_dict[dict]["Table"] = result[0]
        list_dict[dict]["Exact IC"] = result[1]
        list_dict[dict]["Approx IC"] = result[2]
        list_dict[dict]["Approx R"] = result[3]
        print(f"Name of text: {dict}\nExact IC: {list_dict[dict]['Exact IC']}\n"
              f"Approx IC: {list_dict[dict]['Approx IC']}\nApprox R: {list_dict[dict]['Approx R']}\n")
        print(f"Table of Letter Frequency for text string: {dict}\n")
        print_dict_prettytable(list_dict[dict])
        print("\n")


    print("Answering question 4:\n")
    stringy = list_dict["Problem 4"]["String"]

    print("Repeating sequences of 3 characters in Problem 4 text.")
    three_char_sequence = find_repeating_sequences(stringy, 3, 2)
    print(three_char_sequence)
    three_char_factor_set = find_positions_of_repeating_sequences_and_factoring(stringy,
                                                                               three_char_sequence)
    print("Common prime factors of differences in position between three character repeating sequences.")
    print(three_char_factor_set)
    print("\n\n")

    print("Repeating sequences of 4 characters in Problem 4 text.")
    four_char_sequence = find_repeating_sequences(stringy,4,2)
    print(four_char_sequence)
    four_char_factor_set = find_positions_of_repeating_sequences_and_factoring(stringy,four_char_sequence)
    print("Common prime factors of differences in position between four character repeating sequences.")
    print(four_char_factor_set)
    print("\n\n")

    print("Repeating sequences of 5 characters in Problem 4 text.")
    five_char_sequence = find_repeating_sequences(stringy, 5, 2)
    print(five_char_sequence)
    five_char_factor_set = find_positions_of_repeating_sequences_and_factoring(stringy,five_char_sequence)
    print("Common prime factors of differences in position between five character repeating sequences.")
    print(five_char_factor_set)
    print("\n\n")

    print("Repeating sequences of 6 characters in Problem 4 text.")
    six_char_sequence = find_repeating_sequences(stringy, 6, 2)
    print(six_char_sequence)
    six_char_factor_set = find_positions_of_repeating_sequences_and_factoring(stringy,six_char_sequence)
    print("Common prime factors of differences in position between six character repeating sequences.")
    print(six_char_factor_set)
    print("\n\n")

    print("Repeating sequences of 7 characters in Problem 4 text.")
    seven_char_sequence = find_repeating_sequences(stringy, 7, 2)
    print(seven_char_sequence)
    seven_char_factor_set = find_positions_of_repeating_sequences_and_factoring(stringy,seven_char_sequence)
    print("Common prime factors of differences in position between seven character repeating sequences.")
    print(seven_char_factor_set)
    print("\n\n")

    for i in range(3,8):
        print(f"Splitting strings into {i} columns.")
        split = split_string_into_columns(stringy, i)
        print(split)
        print()
        print("Analysis of letter distribution in each column:")
        for j in range(1,i+1):
            temp_result = make_frequency_tables(split[j])[0]
            title = f"Size {i} Keyword, Column {j}"
            print_string_prettytable(temp_result, title)


    return
