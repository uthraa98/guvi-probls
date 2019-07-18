def WordSentence(Sentence1):  
    words = Sentence1.split(" ") 
    newWords = [word[::-1] for word in words] 
    newSentence = " ".join(newWords)   
    return newSentence 
Sentence = input()



print(WordSentence(Sentence1)) 
