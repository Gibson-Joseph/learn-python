# WALRUS OPERATOR
# :=
# This is new operator

# The walrus operator help us to assigns value to variables as part of a larget expression.
# So usually you use it in an expression when something is being evaluated like in an if statement maybe a while statement

a = "Hellooooooooooo"


if len(a) > 10:
    # We are wrirting code and we are repeating ourselves here because we're calculating a length twice.
    print(f"too long {len(a)} elements")

# But with the walrus operator, We can do exactly like above.

if (n := len(a)) > 10:
    print(f"too long {n} elements")

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]

print(a)

# We might not see it a very often. It's essentially a way for us to minimize doing calculations that are similar
