from useful_c231.kasiski_and_IC import *
from string_manip.preprocessing import *

def main():
    cipher_text = "usmoczgrpqbgwjmcyeqrhffcsptxdihtjombvrkydemqgjhrilbhqrgconwcsrgmoezhjztjfiildcxtjlbgsmbefymqstbnipzhhixymwgccvllpepzjvmmdzvusptlztuocimyoeudoeblhltsvfneiqwqhyxbfnzxdkblhaznqvlquzenfbvmscmbhcrgtswtzumpzewtgvpmsoasvrmpfqtdqklrbylzfuxlhwqrvcxrupzefvjsfykxmfnqfpbgclzfusisgkachcmzhkagoriaclmdspytsevwbyikmjbqjqgniyttfpvnixabbeihbkagtnirsvgmvrpbvrkydemqgphsezvsvrocuzbgwedrpzpzfutzpfbtgzgeusmqwxardsiqotmcsqzdelxldjehhytdbtzkmybeinmqhrblujqskzejbfbnarmgdltkmytnqpvsvzlpfxihbjmpvpmusebdjepqcnbltezzbxxupclrwcxysymctihknjabfruzmpxkopblhoixgcbiflikwzswakguorgbrtqbclebfgmmouwgodwlsthkqwmssyhexlagzzdccfzyzvusnaimrabjmtnxoewgoepdsewgudpnicwlucwbykacczishfhkvnpaikmfjdifozgmowggccwquccdwwmffcmhgvgmvrptbthlucqusugyufzzzvgemtagzrgevlodrrmyuzlqcngmvebgsfmffcxhstxqusqrppmffhixwjpfzepdfvtpfdmooitrfdxdqztjjkmctixovpvbmrgymjadgfybjqndfvgrujxdgfycorthgymcyeabwvgrjqqboimgdwmrazzfusiusdhpffvbcdfmohwqrjpgustdhkxptywsijnymwgtgvwqpznssegmxjwtazzfuhwmrvkfphutqypcntoghsxaipiswezsttvfodhbfcvbcdisupzscrgymjhdhybqupfsvfpcwpzhtphsezbgwjtadzzcwezrpepdrzkcdeqnbjmffxihbkagorgnirkcvdqmuzmdpcenicwzfnwtbkblhepdqytpbnbdfjtrbdsvvzvfxzckrtxpulqmzpucuplhcllrpowamytlemcsrvygotbdzpimtdqazvaywpqvfzmrfymmclzfixuhaehrtfzdplmgxttkardctfzdhfmctebgwjucgzzduzogorqsmfnymwjxhyxubjegokectdwmrfxqusqrsotkqwmssrvfzzczpfnrbgqfsexpfvmxkfkbnlsdglkczzchbtesepbgsrgqxpzsckagtbcdgkbmotvxclkqvmuhhkxbtztthzhlt"
    # make sure preprocessing is right
    cipher_dict =  {"String": cipher_text, "Exact IC": 0.00, "Approx IC": 0.00, "Approx R": 0.00,
                                "Table": PrettyTable, "DictSet": {}, "FactorList": set()}
    # make sure all 26 letters are there
    print(f"Number of letters in original text is {len(cipher_text)}")
    print("\n")
    print("Checking that all letters from the alphabet are present in ciphertext.")
    find_missing_alphabet_letters(cipher_text,"cipher_text")
    load_IC_R_FrequencyTable_into_dict(cipher_dict)
    print_IC_R_of_loaded_dict(cipher_dict, "cipher_text")
    print_dict_prettytable(cipher_dict, "cipher text")
    #print_Sequence_and_FactorList(cipher_text,(2,17),2,True)
    #split_strings_print_IC_for_keyword_size(cipher_text,(2,23), True)
    solution = split_strings_find_shift_Es_solve_cipher(cipher_text, 8)
    keyword = solution[1]
    print("Decrypted message: ")
    print(solution[0])
    print("\n")
    print(f"Keyword: {keyword}")
    return
if __name__ == '__main__':
  main()




  #new direction
  #put all of the letter frequency datapoints with their keyword size in a big dataframe with lots of keyword sizes,
  # make a score based on the least difference from the english language frequencies
  # average them across each column in a keyword size and sort to find the one with the least error
  # start messing with that one, work on decoding
