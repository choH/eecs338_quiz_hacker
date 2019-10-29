import json
import difflib


last_name_first_vowel = 'O'


def OS_quiz_tokenizer(input_filename, vowel=None):
    if vowel is not None:
        vowel = vowel.upper()
        vowel_list = ['A', 'E', 'I', 'O', 'U', 'Y']
        if vowel not in vowel_list:
            print("{} is not a proper vowel.".format(vowel))
            return -1
        if vowel in ['U', 'Y']:
            vowel = 'U/Y'

    line_list = []
    word_list = []
    with open(input_filename) as input_file:
        for i in input_file:
            if i.split(' ')[0] == vowel or vowel == None:
                line_list.append(i.split('\n')[0].split(' ', 1)[-1])
                word_list.extend(i.split('\n')[0].split(' ', 1)[-1].split())
    for i in word_list:
        if '-' in i:
            word_list.extend(i.split('-'))
    return line_list, word_list



raw_line_list, raw_word_list = OS_quiz_tokenizer('input.txt')
q_line_list, q_word_list = OS_quiz_tokenizer('input.txt', last_name_first_vowel)


raw_word_len_set = {len(i) for i in raw_word_list}
raw_word_dict = {i:[] for i in raw_word_len_set}
for i in raw_word_list:
    raw_word_dict[len(i)].append(i)
# print(json.dumps(raw_word_dict, indent=4))



def get_match_list(tar, reserve_list=None, thld=0.60):
    reserve_list = raw_word_dict[len(tar)] if reserve_list is None else reserve_list
    reserve_match_dict = {}
    for a_q_reserve in reserve_list:
        reserve_match_dict[a_q_reserve] = difflib.SequenceMatcher(None, tar, a_q_reserve).ratio()
    # print(sorted(reserve_match_dict.items(), key=lambda kv: kv[1])[::-1])
    sorted_q_reserve = [i[0] for i in sorted(reserve_match_dict.items(), key=lambda kv: kv[1])[::-1] if i[1] >= thld]
    del sorted_q_reserve[0]
    # print(sorted_q_reserve)
    return sorted_q_reserve

def try_fill_word(tar, reserve_list=None):
    reserve_list = raw_word_dict[len(tar)] if reserve_list is None else reserve_list
    underline_index_list = [i for (i, x) in enumerate(tar) if x == '_']
    match_list = get_match_list(tar, reserve_list=reserve_list)
    # print(match_list)
    new_tar = tar
    if match_list and underline_index_list:
        for i in underline_index_list:
            # print(i)
            if match_list[0][i] != '_':
                temp_str_list = list(new_tar)
                temp_str_list[i] = match_list[0][i]
                new_tar = "".join(temp_str_list)
            # return try_fill_word(tar, reserve_list[1:])
        # print(new_tar)
        return try_fill_word(new_tar, reserve_list[1:])
    else:
        return new_tar



answer_buffer = []
for a_q_line in q_line_list:
    a_q_word_list = a_q_line.split(' ')
    line_answer_buffer = []
    for a_q_word in a_q_word_list:
        filled_word = try_fill_word(a_q_word)
        line_answer_buffer.append(filled_word)

        if '-' in filled_word and '_' in filled_word:
            hypen_word_token_list = filled_word.split('-')
            hypen_word_token_buffer = [];
            for i in hypen_word_token_list:
                filled_hypen_word_portion = try_fill_word(i)
                hypen_word_token_buffer.append(filled_hypen_word_portion)
            filled_hypen_word = "-".join(hypen_word_token_buffer)

            if filled_hypen_word.count('_') < filled_word.count('_'):
                del line_answer_buffer[-1]
                line_answer_buffer.append(filled_hypen_word)
                # print("Improvement: {} --> {} --> {}".format(a_q_word, filled_word, filled_hypen_word))
            else:
                if not filled_hypen_word == filled_word:
                    del line_answer_buffer[-1]
                    hypen_word_underline_index_list = [i for (i, x) in enumerate(filled_word) if x == '_']
                    for i in hypen_word_underline_index_list:
                        if filled_hypen_word[i] != '_':
                            filled_word[i] =  filled_hypen_word[i]
                    line_answer_buffer.append(filled_word)
                    # print("Collation Improvement: {} --> {} --> {}".format(a_q_word, filled_word, filled_hypen_word))
                # print("No Improvement: {} --> {} --> {}".format(a_q_word, filled_word, filled_hypen_word))


    answer_buffer.append(' '.join(line_answer_buffer))

for i, j in zip(q_line_list, answer_buffer):
    print("{:>30} {} --> {} {}".format(i, ' '*3, ' '*3, j))