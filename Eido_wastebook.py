#text input fields and matching
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "test run\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    @property
    def text(self) -> str:
        return self.get

    def input_string():
      e = Entry(master)

    #each of the next two objects need to have their own text fields - possibly
    #additional text sub=objects
    def mapping_dict(txt_to_connective, txt_to_prop):
      new_mapping = #needs to be two dictionaries but they cant be nested 
      #each needs to be iterable 
      

      def txt_to_connective(input_string, connective):
        #add connective operations 
        connective = ("and", "or", "thus") #and so on
      
      def txt_to_prop(input_string, proposition):
        input = input_string()
        proposition = ("P", "Q", "R", "S", "T") #eventually change to a list
        #fetch relevant proposition by index position

        #dictonary matching - should it take place inside existing objects, 
        #or should it just map the previous two together into a new array
    

    def __init__(self, master, **kwargs):
      tk.Entry.__init__(self, master, **kwargs)

textbox = Text(root)
textbox.grid

textbox.text = "this is text"



root = tk.Tk()
app = Application(master=root)
app.mainloop()


#text input fields and matching
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "test run\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    @property
    def text(self) -> str:
        return self.get

    def input_string():
      e = Entry(master)

    #each of the next two objects need to have their own text fields - possibly
    #additional text sub=objects
    def mapping_dict(txt_to_connective, txt_to_prop):
      new_mapping = #needs to be two dictionaries but they cant be nested 
      #each needs to be iterable 
      

      def txt_to_connective(input_string, connective):
        #add connective operations 
        connective = ("and", "or", "thus") #and so on
      
      def txt_to_prop(input_string, proposition):
        input = input_string()
        proposition = ("P", "Q", "R", "S", "T") #eventually change to a list
        #fetch relevant proposition by index position

        #dictonary matching - should it take place inside existing objects, 
        #or should it just map the previous two together into a new array
    

    def __init__(self, master, **kwargs):
      tk.Entry.__init__(self, master, **kwargs)

textbox = Text(root)
textbox.grid

textbox.text = "this is text"



root = tk.Tk()
app = Application(master=root)
app.mainloop()








!pip install nltk
!pip install pydictionary
!pip install scipy
!pip install matplotlib
!pip install sklearn
!pip install tabulate 


#to do: merge this module with the vector analysis/proposition creation one 

import itertools
import re
from prettytable import PrettyTable #change to tabulate - pretty table is obsolete
import pyparsing
import pandas as pd
import numpy as np
from tabulate import tabulate
import synbank
from Pydictionary import pydictionary
from collections import namedtuple

#create connective - vectorization table to drawn on for 
# id/connective differentiation

OPERATIONS = {
    'not':    (lambda x: not x)
    '-':      (lambda x: not x)
    '~':      (lambda x: not x)
    'it is not the case that': (lambda x: not x)
    'it is false that': (lambda x: not x)




    'or':     (lambda x, y: x or y)
    'nor':     (lambda x, y: not (x or y))
    'xor':     (lambda x, y: x =!y)

    'and':      (lambda x, y: x and y)
    'as well as':  (lambda x, y: x and y)   
    'but':  (lambda x, y: x and y)                
    'also': (lambda x, y: x and y)
    'furthermore': (lambda x, y: x and y)
    'and then within': (lambda x, y: x and y)
    'and then': (lambda x, y: x and y)


    'nand': (lambda x, y: not(x and y))
    
    'implies': (lambda x, y: (not x) or y)
    '=>': (lambda x, y: (not x) or y)
    'therefore': (lambda x, y: (not x) or y)
    'hence': (lambda x, y: (not x) or y)
    
    '<=': (lambda x, y: x or (not y))
    'is implied by': (lambda x, y: x or (not y))
    'is entailed by': (lambda x, y: x or (not y))

}


def recursive_map(func, data):
    ##recursively applies map function to list and all sublists
    if isinstance(data, type)
      return [recursive_map(func, elem) for elem in data]
      else
      return(func, elem)





def string_to_bool:
    #converts string to boolean value
    if string == "true"
      return True
    elif string == "false"
      return False
    return string

def solve_phrase:

    if isinstance(phrase, bool):
      return phrase
    if isinstance(phrase, list):
      #list with list in it
      if len(phrase) == 1 :
        return solve_phrase(phrase[0])
      #single minded operation
      if len(phrase) == 2:
        return OPERATIONS[phrase[0]](solve_phrase(phrase[0]))
      else:
        return OPERATIONS[phrase[1]](solve_phrase[phrase[0]]),
                                      solve_phrase[phrase[2]]
      

def group_operations:
    ##recurseively groups logical operations into lists based on order of opertations
    ##such that each list is just one operation

  #order = not, and, or, implication/reverse implication, biconditional

    if isinstance(phrase, list):
        if len(phrase) == 1
          return phrase
        for operator in ['not', '~', '-', 'it is not the case that', 'it is false that']:
            while operator in phrase:
              index = phrase.index(operator)
              phrase[index] = [operator, group_operations(phrase[index+1])]
              phrase.pop(index+1)
        for operator in ['and', 'nand', 'as well as', 'but', 'also', 'furthermore', 'and then within', 'and then']
            while operator in phrase:
              index = phrase.index(operator)
              phrase[index] = [operator, group_operations(phrase[index-1]),
                               operator, 
                               group_operations(phrase[index+1])]
              phrase.pop(index+1)
              phrase.pop(index-1)

        for operator in ['or', 'nor', 'xor']
            while operator in phrase:
              index = phrase.index(operator)
              phrase[index] = [operator, group_operations(phrase[index-1]),
                               operator,
                               group_operations(phrase[index+1])
              phrase.pop(index+1)
              phrase.pop(index-1)

        for operator in ['implies', '=>', 'therefore', 'hence']
            while operator in phrase:
              index = phrase.index(operator)
              phrase[index] = [operator, group_operations(phrase[index-1]),
                               operator,
                               group_operations(phrase[index+1])
              phrase.pop(index+1)
              phrase.pop(index-1)

         for operator in ['is implied', '<=', 'is entailed by']
            while operator in phrase:
                index = phrase.index(operator)
                phrase[index] = [operator, group_operations(phrase[index-1]),
                                 operator, 
                                 group_operations(phrase[index+1])]
                phrase.pop(index+1)
                phrase.pop(index-1)                 
    return(phrase)


class Truths:
    ##class truths with modules for table formatting, valuation

  def _init_(self, bases = None, phrases = None, ints = True, ascending = False)L
    if not bases:
        raise Exception('Base items are required')
      self.bases = bases
      self.phrases = phrases or []
      self.ints = isinstance
    

      #generate sets of booleans for bases
      if ascending:
          order = [False, True]
      else:
          order = [True, False]

    
    self.base_conditions = list(itertools.product(order, 
                                                  repeat = len(bases)))

    #regex to match whole words in self.bases
    #used to add object context to variables in self.phrases
    self.p = re.compile(r'(?<!\w)(' + '|'.join(self.bases) + r')(?!\w')

    #used in parsing logical operations
    self.to_match = pyparsing.Word(pyparsing.alphanums)
    for items in itertools.chain(self.bases,
                                 [key for key, val in OPERATIONS.items()]):
        self.to_match |= item
      self.parens = pyparsing.nestedExpr('(', ')', content = self.to_match)

  def calculate(self, *args):
      #Evaluates logical value for each expression

      bools = dict(zip(self.bases, args))

      eval_phrases = []
      for phrase in self.phrases:
          #substitute bases in phrase with boolean values as strings
          phrase = self.p.sub(lambda match: str(bools[match.group(0)]), phrase)
          #wrap phrase in parens
          phrase = '('+ phrase + ')'
          #parse the expression using pyparsing
          interpreted = self.parens.parseString(phrase).asList()[0]
          #convert any True or False to bools
          interpreted = recursive_map(string_to_bool, interpreted)
          #group operations
          interpreted = group_operations(interpreted)
          #evaluate the phrase
          eval_phrases.append(solve_phrase(interpreted))

      #add the bases and evaluated phrases to create a single row
      row = [val for key, val for bools.items()] + eval_phrases
      if self.ints:
        return [int(c) for c in row]
      else:
        return row

  def as_pandas(self):
    #table as pandas dataframe

    df_columns = self.bases + self.phrases
    df = pd.DataFrame(columns = df df_columns)
    for conditions_set in self.base_conditions:
        df.loc[len(df)] = self.calculate(*conditions_set)
    df.index = np.arrange(1, len(df) + 1) #index starting in one
    return df

def as tabulate(self, index = True, table_format = 'psql', align = 'center'):
    ##returns table using tabulate package

    table = tabulate(Truths.as_pandas(self)
                    headers = 'keys',
                    tablefmt = table_format, 
                    showindex = index, 
                    colalign = [align] * (len(Truths.as_pandas(self).columns) + index)
    )

    return table

def valuation(self, col_number = -1):
    #evaluates an expression in a table column as a tautology, contradiction, or a contingency

    df = Truths.as_pandas(self)
    if col_number == -1 
      pass
    elif col_number not in range(1, len(df.columns) + 1):
      raise Exception('indexer is out of bounds')
    else:
        col_number = col_number - 1
    
    #below we need to add in a function that sums the final column and divides by the size of the column - should return a float value
    if sum(df.iloc[:, col_number]) == len(df)
      return 'Tautology'
    elif sum(df.iloc[:, col_number]) == 0
      return 'Contradiction'
    else:
      return ((sum(df.iloc[:, col_number]))/col_number)*100

def _str_(self):
    table = Truths.as_tablulate(self, index = False)
    return str(table)







