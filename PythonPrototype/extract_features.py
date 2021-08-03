import nltk
from nltk.tokenize import *
import numpy as np

#--------------------------------------------------------
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
punctuation = ['?',',','!','.',':',';']

char_count= [0] * len(alphabet)
punctuation_count = [0] * len(punctuation)

#--------------------------------------------------------
#             PART OF SPEECH STUFF
#--------------------------------------------------------
#part of speech ratios + lexical variety
# - determiners
# - prepositions
# - pronouns
# - modal auxiliary-verbs -> CAN, COULD, WILL, WOULD
# - adverbs
# - coord-conjuctions
# - nouns
# - proper-nouns
# - adjectives
# - verbs
# - lexical variety = nouns + proper_nouns + adjectives + verbs + adverbs
pronouns_list = ['PRP', 'PRP$', 'WP', 'WP$']
adverbs_list = ['RB' ,'RBR', 'RBS', 'WRB']
adjectives_list = ['JJ', 'JJR', 'JJS']
verbs_list = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

pos_ratios = [0] * 11

avg_sentence_length = 0
avg_word_length = 0
total_words = 0
#--------------------------------------------------------

def main():
    np.set_printoptions(suppress=True)
    

    features = []
    
    text = open("training_set\Abraham Lincoln\Abraham Lincoln___Lincoln Letters.txt").read()

    #total useful char
    t_u_c = total_useful_char(text)

    total_puctuation = count_punctuation(text)

    total_words = len(word_tokenize(text))

    #FEATURES 1 - 26
    letters_frequency(text, t_u_c)

    #FEATURES 27 - 32
    punctuation_frequency(text, total_puctuation)

    #FEATIRES 33 - 44
    part_of_speech_ratios(text, total_words)

    #FEATURES 44 - 45
    avg_sentence_length = average_sentence_length(text)
    avg_word_length = average_word_length(text)

    features.extend(char_count)
    features.extend(punctuation_count)
    features.extend(pos_ratios)
    features.append(avg_sentence_length)
    features.append(avg_word_length)
    features.append(total_words)

    features = np.array(features).reshape(-1,1)
    
    print("\n\n FEATURES final array: \n", features)
    print(features.shape)




def average_word_length(text):

    words = word_tokenize(text)
    sum = 0

    for word in words:
        sum += len(word)

    return sum/len(words)

def average_sentence_length(text):

    sentences = sent_tokenize(text)
    sum = 0

    for sentence in sentences:
        sum += len(word_tokenize(sentence))

    return sum/len(sentences)

def count_punctuation(text):
    return text.count('?') + text.count(',') + text.count('!') + text.count('.') + text.count(':') + text.count(';')

def total_useful_char(text):
    return len(text) - text.count(" ") - text.count("\n")

def letters_frequency(text, tChar):

    for char in text.lower():
        if char in alphabet:
            char_count[alphabet.index(char)] += 1

    for letter in char_count:
        char_count[char_count.index(letter)] /= tChar

def punctuation_frequency(text, total_puctuation):

    for char in text:
        if char in punctuation:
            punctuation_count[punctuation.index(char)] += 1

    for element in punctuation_count:
        punctuation_count[punctuation_count.index(element)] /= total_puctuation

def part_of_speech_ratios(text, total_words):

    words = word_tokenize(text)
    tagged_words = nltk.pos_tag(words)

    # lexical variety = nouns + proper_nouns + adjectives + verbs + adverbs

    for tagged_word in tagged_words:

        is_a_pronoun = [pronoun for pronoun in pronouns_list if(pronoun in tagged_word)]
        is_a_adverb = [adverb for adverb in adverbs_list if(adverb in tagged_word)]
        is_a_adjective = [adjective for adjective in adjectives_list if(adjective in tagged_word)]
        is_a_verb = [verb for verb in verbs_list if(verb in tagged_word)]

        if 'DT' in tagged_word:
            pos_ratios[0] += 1
        elif 'IN' in tagged_word:
            pos_ratios[1] += 1
        elif is_a_pronoun:
            pos_ratios[2] += 1
        elif 'MD' in tagged_word:
            pos_ratios[3] += 1
        elif is_a_adverb:
            pos_ratios[4] += 1
            pos_ratios[10] += 1
        elif 'CC' in tagged_word:
            pos_ratios[5] += 1
        elif ('NN' in tagged_word or 'NNS' in tagged_word):
            pos_ratios[6] += 1
            pos_ratios[10] += 1
        elif ('NNP' in tagged_word or 'NNPS' in tagged_word):
            pos_ratios[7] += 1
            pos_ratios[10] += 1
        elif is_a_adjective:
            pos_ratios[8] += 1
            pos_ratios[10] += 1
        elif is_a_verb:
            pos_ratios[9] += 1
            pos_ratios[10] += 1


    for element in pos_ratios:
        pos_ratios[pos_ratios.index(element)] /= total_words



if __name__ == '__main__':
    main()

