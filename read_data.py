import pandas as pd
import matplotlib as mt
import matplotlib.pyplot as plt
import re
from models.feature_engineering import patterns
import csv
import seaborn as sns


all_labels = []
all_messages  = []

with open('./data/SMSSpamCollection.csv', 'r') as f:
    reader = csv.reader(f)
    
    for row in reader:
         all_messages.append(row[0][4:])
         all_labels.append(row[0][0:4])

        
phone_number_spam_messages = []
special_signs_spam_messages = []
all_caps_spam_messages = []
single_letter_word_messages = []
same_letter_more_than_3x = []


duplicates = []
for message in all_messages:
    if all_messages.count(message) > 1 and message not in duplicates:
        duplicates.append(message)


for message in all_messages: 
    phone_number = re.search(patterns.phone_number_pattern, message)
    
    if phone_number: 
        phone_number_spam_messages.append(message[0])

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

duplicates = []
for message in all_messages:
    if all_messages.count(message) > 1 and message not in duplicates:
        duplicates.append(message)

print(len(duplicates), "length duplicate")


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
print(df, 'df do')
print(ham_spam_data['counts'], 'ham_spam_data[counts]', ham_spam_data['labels'])

plt.pie(ham_spam_data['counts'], labels=ham_spam_data['labels'], autopct='%1.1f%%')



plt.show()

# create a pie chart using seaborn
# colors = ['red', 'green', 'blue', 'yellow', 'pink', 'purple']

# plt.title('Spam messages', fontweight='bold', bbox=dict(facecolor='red', edgecolor='black', boxstyle='round,pad=1'))
# plt.pie(showers['values'],  labels=showers['labels'], autopct='%1.1f%%', startangle=90, shadow=True,  textprops={'fontsize': 10})


# plt.show()
