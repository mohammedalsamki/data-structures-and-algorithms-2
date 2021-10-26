from stack_and_queue.stack_and_queue import Stack

def validate_brackets(text):
  stack = Stack()
  temp=[]
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



