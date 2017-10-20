from spacy.en import English
from numpy import dot
from numpy.linalg import norm
# from subject_object_extraction import findSVOs

def get_info(parsedData):
    for i, token in enumerate(parsedData):
        print("original:", token.orth, token.orth_)
        print("lowercased:", token.lower, token.lower_)
        print("lemma:", token.lemma, token.lemma_)
        print("shape:", token.shape, token.shape_)
        print("prefix:", token.prefix, token.prefix_)
        print("suffix:", token.suffix, token.suffix_)
        print("log probability:", token.prob)
        print("Brown cluster id:", token.cluster)
        print("----------------------------------------")
        if i > 1:
            break

def message_content_details(parsedData):
    # Let's look at the part of speech tags of the first sentence
    for span in parsedData.sents:
        sent = [parsedData[i] for i in range(span.start, span.end)]
        break

    for token in sent:
        print(token.orth_, token.pos_)

def message_content_dependencies(parsedData):
    # shown as: original token, dependency tag, head word, left dependents, right dependents
    for token in parsedData:
        print(token.orth_, token.dep_, token.head.orth_, [t.orth_ for t in token.lefts], [t.orth_ for t in token.rights])


def message_content_named_entities(parsedData):
    for token in parsedData:
        print(token.orth_, token.ent_type_ if token.ent_type_ != "" else "(not an entity)")

    print("-------------- entities only ---------------")
    # if you just want the entities and nothing else, you can do access the parsed examples "ents" property like this:
    ents = list(parsedData.ents)
    for entity in ents:
        print(entity.label, entity.label_, ' '.join(t.orth_ for t in entity))

def message_content_messy_data(parsedData):
    for token in parsedData:
        print(token.orth_, token.pos_, token.lemma_)


def word_vector_representations(word):
    parser = English()
    # you can access known words from the parser's vocabulary
    nasa = parser.vocab[word]

    # cosine similarity
    cosine = lambda v1, v2: dot(v1, v2) / (norm(v1) * norm(v2))

    # gather all known words, take only the lowercased versions
    allWords = list({w for w in parser.vocab if w.has_repvec and w.orth_.islower() and w.lower_ != "nasa"})

    # sort by similarity to word
    allWords.sort(key=lambda w: cosine(w.repvec, nasa.repvec))
    allWords.reverse()
    print("Top 10 most similar words to " + word + ":")
    for word in allWords[:10]:   
        print(word.orth_)


# def message_SVOs(parsedData):
#     print(findSVOs(parsedData))

def parse_message(message):
    parser = English()
    parsedData = parser(message)

    get_info(parsedData)
    message_content_details(parsedData)
    message_content_dependencies(parsedData)
    message_content_named_entities(parsedData)
    message_content_messy_data(parsedData)

# dump
input_message = "he and his brother shot me and my sister"
print("input_message: " + input_message)
parse_message(input_message)