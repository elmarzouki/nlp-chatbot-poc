from spacy.en import English
from numpy import dot
from numpy.linalg import norm
# from subject_object_extraction import findSVOs
import json

"""
    tokenization, sentence recognition, part of speech tagging, lemmatization,
    dependency parsing, and named entity recognition
"""


def get_message_info(parsedData):
    """
    :param parsedData: data after being parsed by the en parser
    :return: message info in json
    """
    message_info = {}
    token_info = {}
    for i, token in enumerate(parsedData):
        token_info['original'] = str(token.orth) + " " + str(token.orth_)
        token_info['lowercased'] = str(token.lower) + " " + str(token.lower_)
        token_info['lemma'] = str(token.lemma) + " " + str(token.lemma_)
        token_info['shape'] = str(token.shape) + " " + str(token.shape_)
        token_info['prefix'] = str(token.prefix) + " " + str(token.prefix_)
        token_info['suffix'] = str(token.suffix) + " " + str(token.suffix_)
        token_info['log_probability'] = str(token.prob)
        token_info['Brown_cluster_id'] = str(token.cluster)
        message_info[i] = token_info
        if i > 1:
            break
    json_data = json.dumps(message_info)
    return json_data


def get_message_content_sents(parsedData):
    """
    :param parsedData:  data after being parsed by the en parser
    :return: sentence recognition
    """
    sents = {}
    # the "sents" property returns spans
    # spans have indices into the original string
    # where each index value represents a token
    for i, span in enumerate(parsedData.sents):
        # for span in parsedData.sents:
        # go from the start to the end of each span, returning each token in the sentence
        # combine each token using join()
        sent = ''.join(parsedData[i].string for i in range(span.start, span.end)).strip()
        sents[i] = sent

    json_data = json.dumps(sents)
    return json_data


def get_message_content_speech_tagging(parsedData):
    """
    speech tagging
    :param parsedData: data after being parsed by the en parser
    :return: message_content_speech_tagging
    """
    speech_tagging = {}
    for span in parsedData.sents:
        sent = [parsedData[i] for i in range(span.start, span.end)]
        break

    # for token in sent:
    for i, token in enumerate(sent):
        speech_tagging[i] = token.orth_ + " " + token.pos_

    json_data = json.dumps(speech_tagging)
    return json_data


def get_message_content_dependencies(parsedData):
    """
    dependency parsing
    :param parsedData:  data after being parsed by the en parser
    :return: message_content_dependencie
    """
    dependencies = {}
    # shown as: original token, dependency tag, head word, left dependents, right dependents
    for token in parsedData:
        dependencies[token] = token.orth_ + " " + token.dep_ + " " + token.head.orth_ + " " + \
                              [t.orth_ for t in token.lefts] + " " + [t.orth_ for t in token.rights]

    json_data = json.dumps(dependencies)
    return json_data


def get_message_content_named_entities(parsedData):
    """
    named entity recognition
    :param parsedData: data after being parsed by the en parser
    :return: message_content_named_entities
    """
    entities = {}
    all_entities = {}
    named_entities = {}
    # for token in parsedData:
    for i, token in enumerate(parsedData):
        all_entities[i] = token.orth_ + " " + token.ent_type_ if token.ent_type_ != "" else "(not an entity)"

    entities['all_entities'] = all_entities

    # if you just want the entities and nothing else, you can do access the parsed examples "ents" property like this:
    ents = list(parsedData.ents)
    # for entity in ents:
    for i, entity in enumerate(ents):
        named_entities[i] = entity.label + " " + entity.label_ + " " + ' '.join(t.orth_ for t in entity)

    entities['named_entities'] = named_entities

    json_data = json.dumps(entities)
    return json_data


def get_message_content_messy_data(parsedData):
    """
    spaCy is trained to attempt to handle messy data, including emoticons and other web-based features
    :param parsedData: data after being parsed by the en parser
    :return: messy_data
    """
    messy_data = {}
    # for token in parsedData:
    for i, token in enumerate(parsedData):
        messy_data[i] = token.orth_ + " " + token.pos_ + " " + token.lemma_

    json_data = json.dumps(messy_data)
    return json_data


def get_word_vector_representations(word):
    """
    spaCy has word vector representations built in!
    :param word: a word you wanna get it's vector representations
    :return: word vector representations
    """
    parser = English()
    word_vector_representations = {}
    # you can access known words from the parser's vocabulary
    nasa = parser.vocab[word]

    # cosine similarity
    cosine = lambda v1, v2: dot(v1, v2) / (norm(v1) * norm(v2))

    # gather all known words, take only the lowercased versions
    allWords = list({w for w in parser.vocab if w.has_repvec and w.orth_.islower() and w.lower_ != "nasa"})

    # sort by similarity to word
    allWords.sort(key=lambda w: cosine(w.repvec, nasa.repvec))
    allWords.reverse()

    # Top 10 most similar words to word
    # for word in allWords[:10]:
    for i, word in enumerate(allWords[:10]):
        word_vector_representations[i] = word.orth_

    json_data = json.dumps(word_vector_representations)
    return json_data


# def message_SVOs(parsedData):
#     print(findSVOs(parsedData))

def parse_message(message):
    parser = English()
    parsedData = parser(message)
    parsing_results = {}

    # print("\n message_info :\n")
    message_info = get_message_info(parsedData)
    # print(message_info)
    parsing_results['info'] = message_info

    # print("\n message_content_sents :\n")
    message_content_sents = get_message_content_sents(parsedData)
    # print(message_content_sents)
    parsing_results['sents'] = message_content_sents

    # print("\n message_content_speech_tagging :\n")
    message_content_speech_tagging = get_message_content_speech_tagging(parsedData)
    # print(message_content_speech_tagging)
    parsing_results['speech_tagging'] = message_content_speech_tagging

    # print("\n message_content_dependencies :\n")
    message_content_dependencies = get_message_content_dependencies(parsedData)
    # print(message_content_dependencies)
    parsing_results['dependencies'] = message_content_dependencies

    # print("\n message_content_named_entities :\n")
    message_content_named_entities = get_message_content_named_entities(parsedData)
    # print(message_content_named_entities)
    parsing_results['entities'] = message_content_named_entities

    # print("\n message_content_messy_data :\n")
    message_content_messy_data = get_message_content_messy_data(parsedData)
    # print(message_content_messy_data)
    parsing_results['messy_data'] = message_content_messy_data

    # print("\n word_vector_representations :\n")
    word_vector_representations = get_word_vector_representations(message[0])
    # print(word_vector_representations)
    parsing_results['word_vector_representations'] = word_vector_representations

    json_data = json.dumps(parsing_results)
    return json_data


# dump
print(parse_message(input("enter a message to be parsed: \n")))