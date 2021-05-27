# We will talk about conditional logic here.

is_old = True
is_licenced = True

if is_old:
    print("You are old enough to drive.")
else:
    print("You are to young to drive!")

is_old = False
is_licenced = True

if is_old:
    print("You are old enough to drive.")
elif is_licenced:
    print("You have licence to drive.")
else:
    print("You are to young to drive!")

is_old = False
is_licenced = False

if is_old:
    print("You are old enough to drive.")
elif is_licenced:
    print("You have licence to drive.")
else:
    print("You are to young to drive!")

is_old = True
is_licenced = True

if is_old and is_licenced:
    print("You have all the qualification to drive.")
else:
    print("You are to young to drive!")

print("Happy Coding... :-)")