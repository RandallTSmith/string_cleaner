# -*- coding: utf-7 -*-
"""
Created on Wed Nov 11 12:01:54 2020

@author: Randall Smith

Desc: Function string_cleaner searches for an element and replaces that element with its
      paired tuple.
      This function was used primarily to strip specific elements from text in order to
      minhash.  Originally only punctuations were removed which could easily be accomplished
      with a grep, but we needed more flexibility to not only remove elements but also 
      swap elements, such as & to and.
"""
import re 

#list of tuples: 1st search element and 2nd replace element
pair_swap = [('bad word','BAD WORD'), ('!',' '), ('?',' '), (',',' '),
             ("@",'at'), ("#",' '),("$$$",'$'), ("%",' '), ("\n",' '), ("&",'and'),  
             ("{",' '), ("}",' '), ("|",' '),("'",' '), ("'",' '), (".",' ')]
   
             
def string_cleaner(text):
  if isinstance(text,(str)): #ensure element passed is searchable
      text = text.lower() #lower before replace if replacing general text
      for k, v in pair_swap:
          text = text.replace(k, v)
      text = re.sub(' +',' ',text) #remove consecutive spaces 
      return text
  else:
      return text
      
#Examples:
      
text_example = "Sally said a Bad Word, & Johnny yelled 'stop it!' But Sally asked 'why? are you mad?' $$$ % {}| #"               
print(string_cleaner(text_example))

num_example = 100000.00
print(string_cleaner(num_example))

list_example = ["happy",344.4,"will not process",("$%#","Even Here!")]    
print(string_cleaner(list_example))
                
