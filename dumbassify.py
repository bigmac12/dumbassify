from cgitb import text
import time
import re
from string import punctuation

word_substitutions = {
    'angry': 'aggro',
    'owned': 'pwned',
    'says': 'sez',
    'son': 'slon',
    'wrecked': 'rekt',
}


def check_word(word):
    if word in word_substitutions:
        word = word_substitutions[word]
    else:
        if word[-2:].strip().lower() == 'ed':
            word = ''.join([word[:-2], 't'])

    return word


# Attempts to open a file. If that fails, assume it's just a string and dumbassify it.
def dumbassify(text_or_source, dump_to_file=False, dump_file_name='dumbassify.txt'):
    start = time.time()
    word_buffer = list()

    # Side-effecty AF, but whatever. 
    try:
        source = open(text_or_source, 'r').read()  # Not every file name will have a dot, so I don't bother checking.
    except:
        if not isinstance(text_or_source, str):
            raise ValueError('"text_or_source" must be a string or file name.')

        source = text_or_source

    word_buffer = source.split(' ')
    # print(word_buffer[0])
    
    dumbassified_text = ' '.join([check_word(word) for word in word_buffer])
    print(dumbassified_text)

    # TODO
    if dump_to_file:
        # with open(dump_file_name, 'w') as dump_file:
        #   dump_file.write(mockified_text)
        pass  

    return dumbassified_text, len(source.split(' ')), time.time()-start


def dump_stats(data):
    print("{} \nDumbassified {} words in {:0.2f}s\n".format(data[0], data[1], data[2]))


def dummy_file(name='dummy.txt'):
    with open(name) as f:
        f.write('hi')
    f.close()


if __name__ == '__main__':
   dumbassify('dumbassify_1.txt')
