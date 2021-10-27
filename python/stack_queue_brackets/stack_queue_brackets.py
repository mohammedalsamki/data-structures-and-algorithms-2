from stack_and_queue.stack_and_queue import Stack

def validate_brackets(text):
  """
    Method representing whether or not the brackets in the string are balanced

    Arg: text is string to be validated
    Return : Boolean if the string is balanced
  """

  stack = Stack()
  for paren in text:

    if paren == '(' or paren == '[' or paren == '{':
      stack.push(paren)
    else:

      if not stack.top:
        return True
      else:
        top = stack.top.value
        if paren == ')' and top == '(' or \
        paren == ']' and top == '[' or \
        paren == '}' and top == '{':
          stack.pop()
  if not stack.top:
    return True
  else:
    return False



