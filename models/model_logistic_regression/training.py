import re
import feature_engineering

def has_phone_number(message):
    phone_number = re.search(feature_engineering.phone_number_pattern, message)
    if phone_number:
        return 1
    else:
        return 0

def has_strange_pattern(message):
    strange_pattern = re.search(feature_engineering.strange_signs_pattern, message)

    if strange_pattern:
        return 1
    else:
        return 0
    

def has_all_caps_pattern(message):
    all_caps_pattern_message = re.search(feature_engineering.all_caps_pattern, message)
    if all_caps_pattern_message:
        return 1
    else:
        return 0

def has_single_word_message_pattern(message):
    single_letter_words_message = re.search(feature_engineering.one_letter_words_in_sentence_other_than_i_id_a_u, message)

    if single_letter_words_message:
        return 1
    else:
        return 0


def has_same_letter_more_than_3_times_number(message):
    same_letter_more_than_3_times_message = re.search(feature_engineering.same_letter_more_than_3x_pattern, message)
    if same_letter_more_than_3_times_message:
        return 1
    else:
        return 0
            
