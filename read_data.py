import pandas as pd
import matplotlib as mt
import matplotlib.pyplot as plt
import re
from patterns import patterns
import csv
import seaborn as sns


mt.use('TkAgg')

all_messages = []

good_messages = []

with open('/mnt/c/Users/flore/Downloads/SMSSpamCollection.csv', 'r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        # getting rid of ham\t as part of cleaning the data 
        # all_messages.append(row)
        
        [all_messages.append(x) for x in row]

        # all_messages.append(row)

# print(all_messages)

phone_number_spam_messages = []
special_signs_spam_messages = []
all_caps_spam_messages = []
single_letter_word_messages = []
same_letter_more_than_3x = []


for message in all_messages: 
    phone_number = re.search(patterns.phone_number_pattern, message)
    
    if phone_number: 
        phone_number_spam_messages.append(message)

    strange_pattern = re.search(patterns.strange_signs_pattern, message)

    if strange_pattern: 
        special_signs_spam_messages.append(message)
        
    all_caps_pattern_message = re.search(patterns.all_caps_pattern, message)

    if all_caps_pattern_message: 
        all_caps_spam_messages.append(message)

    single_letter_words_message = re.search(patterns.one_letter_words_in_sentence_other_than_i_id_a_u, message)
    
    
    if single_letter_words_message: 
        single_letter_word_messages.append(message)
    
    same_letter_more_than_3_times_message = re.search(patterns.same_letter_more_than_3x_pattern, message)
    
    if same_letter_more_than_3_times_message: 
        same_letter_more_than_3x.append(message)
    
    
    


all_messages__count = len(all_messages)
same_letter_more_than_3x_count = len(same_letter_more_than_3x)
all_caps_spam_messages_count = len(all_caps_spam_messages)
special_signs_spam_messages_count = len(special_signs_spam_messages)
phone_number_spam_messages_count = len(phone_number_spam_messages)
single_letter_word_messages_count = len(single_letter_word_messages)

print(all_messages__count, 'all_messages__count')
print(same_letter_more_than_3x_count, 'same_letter_more_than_3x_count')
print(all_caps_spam_messages_count, 'all_caps_spam_messages_count')
print(special_signs_spam_messages_count, 'special_signs_spam_messages_count')
print(phone_number_spam_messages_count, 'phone_number_spam_messages_count')
print(single_letter_word_messages_count, 'single_letter_word_messages_count')


showers = {'labels': ['other patterns', "Same Letter words", 'All caps', 
         "phone #", "single letter word"],
        'values': [all_messages__count, same_letter_more_than_3x_count, all_caps_spam_messages_count,
                    phone_number_spam_messages_count, single_letter_word_messages_count,
                      ]}

df = pd.DataFrame(showers)

count_ham= 0
for x in all_messages:
    if x[0:3]=='ham':
        count_ham += 1

count_spam= 0
for x in all_messages:
    if x[0:4]=='spam':
        count_spam += 1

        

print(count_ham, 'count_ham')
print(count_spam, 'count_spam')

counts = [count_ham, count_spam] 
labels =  ['not spam', 'spam']
colors = {'not spam': 'blue', 'spam': 'red'}
data = {'labels': labels, 'counts': counts}
sns.set_style('whitegrid')
sns.color_palette('pastel')
sns.set_palette(sns.color_palette(colors.values()))
ham_spam_data = pd.DataFrame(data)
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, label=label) for label, color in colors.items()]
plt.legend(handles=legend_elements)

df = pd.DataFrame(ham_spam_data)

sns.set_style('darkgrid')
plt.title('Spam vs Non-spam messages')

plt.pie(ham_spam_data['counts'], labels=ham_spam_data['labels'], autopct='%1.1f%%')



plt.show()

# create a pie chart using seaborn
plt.title('Spam messages')
plt.pie(df['values'], labels=df['labels'], autopct='%1.1f%%', startangle=90)


# plt.show()
