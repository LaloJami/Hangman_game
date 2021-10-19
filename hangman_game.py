import random
import os

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

def compare_word(word, word_dic, letter):
  if letter in word_dic and word_dic[letter] == False:
    word_dic[letter] = True
    msg = "Great!"
    update_word_screen(word,word_dic, msg)
    return word_dic
  elif letter in word_dic and word_dic[letter] == True:
    msg = "You already select this letter"
    update_word_screen(word,word_dic, msg)
    return word_dic
  elif letter not in word_dic:
    msg = "ups, select other letter."
    update_word_screen(word,word_dic, msg)
    return word_dic
  

def input_letter():
  words = read_file()
  w = select_word(words)
  d = dictionary_words(w)
  word = d
  update_word_screen(w, word)
  while True:
    try:
      letter = input("Type a letter and press enter.\n")
      if letter.isnumeric() == True:
        msg="You must type a letter, not a number"
        update_word_screen(w,word, msg)
        raise ValueError
      word = compare_word(w, word, letter)
      if False not in word.values():
        msg = "Congratulation!"
        update_word_screen(w,word, msg)
        break
    except ValueError:
      pass
      

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
  random_word = word_list[random.randint(0,len(word_list)-1)]
  random_word = random_word[:-1]
  return random_word

def dictionary_words(list_word):
  dic_word = {word: False for word in list_word}
  return dic_word

def update_word_screen(word, word_dic, msg = '#'):
  os.system("clear")
  print_title()
  print('Your word has '+str(len(word))+' letters:')
  word_show = ''
  for n in word:
    if word_dic[n] == False:
      word_show += '_'
    else:
      word_show += n

  if msg != '#':
    word_show += '\n' + msg
  print(word_show)

def run():
  input_letter()

if __name__ == '__main__':
  run()