import random

def primary():
  f = open("quotes.txt", encoding='utf-8')
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1

  out = ''
  for x in range(5):
    rnd = random.randint(0, last)    
    out += quotes[rnd].rstrip()
  print(out)

if __name__== "__main__":
  primary()
