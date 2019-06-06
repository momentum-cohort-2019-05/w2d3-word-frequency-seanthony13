import operator
import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


# 
f = open("seneca_falls.txt")
text_to_read = (f.read())
lower_case_text = text_to_read.lower()
clean_text = re.sub('[^A-Za-z]', ' ', lower_case_text)
split_word_text = clean_text.split()
# that splits the words
list_of_words = []
for word in split_word_text:
    if word not in STOP_WORDS:
        list_of_words.append(word)


    # Keep count of how often word is used
def get_second_item(seq):
    return seq[1]

def print_freq(frequency):
    print("\n\nFrequency\n==========")
    for word, frq in frequency:
        print(word, frq)
def count_freq(text):

#     # create an empty dictionary
    master_list = {}
#     # create a for loop
    for word in list_of_words:
        if master_list.get(word) == None:
            master_list[word] = 1
        else: 
            master_list[word] += 1
#     # now we creat a list because sort dictiionary the way we need to
    sorted_list = sorted(master_list.items(), key=operator.itemgetter(1), reverse=True)
#     # reverse=True so that it sorts in descending instead of ascending order
    print(sorted_list)

count_freq(list_of_words)

    # Use dictionary to print out frequency


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
