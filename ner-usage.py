import spacy
from spacy import displacy

# text = """Uber blew through $1 million a week"""
# text = """cats are too tall and they pretend to care about your feelings"""
# text = """President George W. Bush reacts to applause during his State of the Union Address at the Capitol, Tuesday,
# Jan. 31, 2006. White House photo by Eric DraperEvery time I'm invited to this rostrum, I'm humbled by the privilege,
# and mindful of the history we've seen together. We have gathered under this Capitol dome in moments of national
# mourning and national achievement. We have served America through one of the most consequential periods of our
# history -- and it has been my honor to serve with you. """

text = """Keeping America competitive requires affordable energy. And here we have a serious problem: America is
addicted to oil, which is often imported from unstable parts of the world. The best way to break this addiction is
through technology. Since 2001, we have spent nearly $10 billion to develop cleaner, cheaper, and more reliable
alternative energy sources -- and we are on the threshold of incredible advances. """

print("loading model...")
# nlp = spacy.load('en_core_web_sm')
nlp = spacy.load('en_core_web_md', disable=['parser', 'tagger'])
print(nlp.pipe_names)
# nlp = spacy.load('model_from_en_sm')
# nlp = spacy.load('model_from_blank_en')
# nlp = spacy.load('model_for_new_entity')
# nlp = spacy.blank('en')
# nlp = spacy.load('model')
doc = nlp(text)

# doc = [token for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
# for token in doc:
#     print(token.text)

# print the entity and its label
for entity in doc.ents:
    if entity.text != '\n':
        print(entity.text, entity.label_)

# print token and its entity label in doc
# for token in doc:
#     entity = [token.text, token.ent_iob_, token.ent_type_]
#     print(entity)

# entity = [token for token in doc if token.ent_iob_!= 'O']
# for ent in entity:
#     print(ent.text, ent.ent_iob_, ent.ent_type_)

# visualize the entity
# displacy.serve(doc, style='ent')