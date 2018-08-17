import spacy
from spacy.gold import GoldParse
from spacy.tokens import Doc

text = """Rats make good pets"""

print("loading model...")
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

for entity in doc.ents:
    if entity.text != '\n':
        print(entity.text, entity.label_)

doc = Doc(nlp.vocab, [u'Rats', u'make', u'good', u'pets'])
gold = GoldParse(doc, [u'U-ANIMAL', u'O', u'O', u'O'])


