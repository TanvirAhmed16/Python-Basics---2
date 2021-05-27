'''
Ternary Operator -  It is basically the same as if...else statement but it is a shortcut way.
'''
# Syntax - statement if condition_is_true else statement if condition_is_false.

is_friend = True

can_message = "Message Allowed." if is_friend else "Not allowed to message."
print(can_message)

is_friend = False

can_message = "Message Allowed" if is_friend else "Not allowed to message."
print(can_message)