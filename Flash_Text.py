#Flash text is an amazing new library which allows us to find and replace words in a document.
#It uses a tree data structure called Trie for efficient information storage and retrieval.
#Both finding and replacement happens over a single pass.

from flashtext import KeywordProcessor
document="""Welcome to Fractal's World.Fractal Analytics is one of the leading analytics companies in India"""
processor=KeywordProcessor()
processor.add_keyword('Fractal')
found=processor.extract_keywords(document)
print(found) 

#Searching for synonyms
processor.add_keywords_from_dict({'Fractal':['Fractal',"Fractal's"]})
found=processor.extract_keywords(document)
print(found) 

#Listing the location of the keywords
processor.add_keywords_from_dict({'Fractal':['Fractal',"Fractal's"]})
found=processor.extract_keywords(document,span_info=True)
print(found) 
