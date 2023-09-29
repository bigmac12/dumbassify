import time
from string import punctuation

word_substitutions = {
    'angry': 'aggro',
    'owned': 'pwned',
    'says': 'sez',
    'son': 'slon',
    'wrecked': 'rekt',
}


def replace_word(word):
    if word in word_substitutions:
        word = word_substitutions[word]
    else:
        if word[-2:].strip().lower() == 'ed':
            word = ''.join([word[:-2], 't'])

    return word


# Attempts to open a file. If that fails, assume it's just a string and dumbassify it.
def dumbassify(text_source, dump_to_file=False, dump_file_name='dumbassify.txt'):
    start = time.time()

    try:
        with open(text_source, 'r') as source_file:
            source = source_file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {text_source} not found.")
    
    except Exception as e:
        raise Exception(f"Error: {e}")

    dumbassified_text = ' '.join([replace_word(word) for word in source.split(' ')])

    print(dumbassified_text)

    if dump_to_file:
        with open(dump_file_name, 'w') as dump_file:
          dump_file.write(dumbassified_text)

    return dumbassified_text, len(source.split(' ')), time.time()-start


def dump_stats(data):
    text, word_count, time_elapsed = data
    print(f"{text} \nDumbassified {word_count} words in {time_elapsed:.2f}s\n")


def create_dummy_file(name='dummy.txt'):
    with open(name, 'w') as f:
        f.write('hi')

    f.close()


if __name__ == '__main__':
   dumbassify('dumbassify_1.txt')
