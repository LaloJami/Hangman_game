import random

def print_title():
  text_title = """
    888    888                                                            
    888    888                                                            
    888    888                                                            
    8888888888  8888b.  88888b.   .d88b.  88888b.d88b.   8888b.  88888b.  
    888    888     "88b 888 "88b d88P"88b 888 "888 "88b     "88b 888 "88b 
    888    888 .d888888 888  888 888  888 888  888  888 .d888888 888  888 
    888    888 888  888 888  888 Y88b 888 888  888  888 888  888 888  888 
    888    888 "Y888888 888  888  "Y88888 888  888  888 "Y888888 888  888 
                                      888                                 
                                Y8b d88P                                 
                                 "Y88P"                                  
                .d8888b.                                                  
              d88P  Y88b                                                 
              888    888                                                 
              888         8888b.  88888b.d88b.   .d88b.                  
              888  88888     "88b 888 "888 "88b d8P  Y8b                 
              888    888 .d888888 888  888  888 88888888                 
              Y88b  d88P 888  888 888  888  888 Y8b.                     
               "Y8888P88 "Y888888 888  888  888  "Y8888
                          
                          by Eduardo Jami 
  """
  return print(text_title)

def input_letter():
  while True:
    try:
      letter = input("Type a letter and press enter.\n")
      if letter.isnumeric() == True:
        raise ValueError
      print(letter)
      break
    except ValueError:
      print("You must type a letter, not a number")

def read_file():
  words = []
  with open('./words_guessing.txt', 'r', encoding='utf-8') as f:
    for line in f:
      words.append(line)

  if len(words) == 0:
    print("Empty File")
  else:
    return words

def select_word(word_list):
  random_word = word_list[random.randint(0,len(word_list))]
  return random_word

def run():
  print_title()
  words = read_file()
  print(select_word(words))
  input_letter()

if __name__ == '__main__':
  run()