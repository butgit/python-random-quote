def primary():
  f = open("quotes.txt", encoding='utf-8')
  quotes = f.readlines()
  f.close()

  print(quotes[0])

if __name__== "__main__":
  primary()
