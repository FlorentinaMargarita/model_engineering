# patterns
phone_number_pattern = r"\d{4,}"
strange_signs_pattern = r"(\$[@$%&*!#?&ltgt]){2,}"
all_caps_pattern = r"^[A-Z\s\W]+$"
one_letter_words_in_sentence_other_than_i_id_a_u = r"\b(?!(i|I|u|U|a|A|i'd|I'd)\b)\w\b.*?\b(?!(i|I|u|U|a|A|i'd|I'd)\b)\w\b"
same_letter_more_than_3x_pattern = r"\w*(\w{1})\1{2,}(?<!\.)\w*"