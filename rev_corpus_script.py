# file = open("corpus.txt",r)
# words = file.read().split()
# rev_words = words[::-1]
# file2 = open("rev_corpus.txt",w)
# file2.write(rev_words)

with open('corpus.txt','r',encoding='utf-8') as f, open('rev_corpus.txt', 'w',encoding='utf-8') as g:
    words = f.read().split()
    words = words[::-1]
    data = ' '.join(words)
    g.write(data)
