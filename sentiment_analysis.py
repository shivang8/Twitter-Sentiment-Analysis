import sys

def sentiment_words_input(words):
  scores = {}
  for line in words:
    l = line.lower()
    term, score = l.split("\t")
    scores[term] = int(score)
  return scores

def tweets_seperator(dataset):
  tweets = []
  for line in dataset:
    l = line.lower()
    tweets.append(l)
  return tweets

def phase2(tweet_text,sentiment,new):
  lexicon = {}
  for word in new:
      positive = 0
      negetive = 0
      total = 0
      for tweet in range(0,len(tweet_text)):
          line = tweet_text[tweet].split()
          if word in line:
              if sentiment[tweet] > 0:
                  positive += 1
              elif sentiment[tweet] < 0:
                  negetive += 1
              total += 1
      lexicon[word] = (positive - negetive + 0.0)/total
  f = open("output_lexicon.txt", "w")
  for n in lexicon:
      f.write(str(n) + "\t" + str(lexicon[n]) + "\n")
  f.close()

def analysis(tweet_text,scores):
  symbols=['!','@','#','$','%','^','&','*','(','0','_','-','+','=','~','{','}','[',']',';',':','"',',','<','>','.','?','/','|','\'','\\','1','2','3','4','5','6','7','8','9','0']
  common_words=["with" ,"at" ,"from" ,"into" ,"during" ,"including" ,"until" ,"against" ,"among" ,"throughout" ,"despite" ,"towards" ,"upon" ,
"concerning" ,"of" ,"to" ,"in" ,"for" ,"on" ,"by" ,"about" ,"like" ,"through" ,"over" ,"before" ,"between" ,"after" ,"since" ,"without" ,"under" ,
"within" ,"along" ,"following" ,"across" ,"behind" ,"beyond" ,"plus" ,"except" ,"but" ,"up" ,"out" ,"around" ,"down" ,"off" ,"above" ,"near" ,
 "is" ,"are" ,"am" ,"why" ,"how" ,"would" ,"should" ,"where" ,"what" ,"who" ,"when" ,"whom" ,"whose" ,"shall" ,"will" ,"did" ,"does" ,"do" ,
"you" ,"was" ,"were" ,"have" ,"has" ,"as" ,"be" ,"can" ,"could" ,"each" ,"every" ,"get" ,"he" ,"she" ,"I", "if" ,"it", "its" ,"may" ,"me" ,
"most" ,"Mr" ,"Mrs" ,"my" ,"oh" ,"ok" ,"once" ,"or" ,"our" ,"pm" ,"say" ,"so" ,"soon" ,"southern" ,"still" ,"such" ,"that" ,"this" ,"those", "them" ,"their" ,"thus" ,
"under" ,"up" ,"us" ,"we" ,"within" ,"yet"  ,"your" ,"themselves" ,"ourselves", "myself" ,"yourself" ,"itself","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

  sentiment_score = []
  new = []
  f = open("output_sentiment_score.txt", "w")
  for tweet in tweet_text:
      sentiment = 0
      flag = 1
      parts = tweet.split()
      for p in parts:
          if p in common_words:
              pass
          elif p == 'not':
            flag = -1
          else:
              if scores.has_key(p):
                  sentiment += (scores[p] * flag)
                  flag = 1
              else:
                  if p not in new:
                      for i in p:
                          if i in symbols:
                              break
                      else:
                          new.append(p)
      f.write(str(sentiment) + "\n")
      sentiment_score.append(int(sentiment))
  f.close()
  phase2(tweet_text,sentiment_score,new)

def main():
  words = open(sys.argv[1])
  tweets = open(sys.argv[2])

  scores = {}
  tweet_text = []

  scores = sentiment_words_input(words)

  tweet_text = tweets_seperator(tweets)

  analysis(tweet_text,scores)

if __name__=='__main__':
  main()
