SNAKE = r""" \
  \    __
   \  {0O}
      \__/
      /^/
     ( (              
     \_\_____
     (_______)
    (_________()Oo
"""

def buble(message):
    bubble_length = len(message) + 2
    return f"""
 {"-" * bubble_length}
( {message} )
 {"-" * bubble_length}"""
 
def say(message):
    print(buble(message))
    print(SNAKE)