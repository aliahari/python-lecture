xgramPost = {"Alice":[("Wow! Iam finally in Karlsruhe!","shorturl.at/chDUX"), ( "Great music @ AKK","shorturl.at/aorP1")], "Bob":[("Great time at python class!","shorturl.at/wxFLR"),("I just learned about lists!","")]}
for key, value in xgramPost.items():
    print(key)
    print(value)
    print("------------")
for key in xgramPost.keys():
    print(key)
    print("------------")
for value in xgramPost.values():
    print(value)
    print("------------")

users = xgramPost.keys()
print(users)
for user in users:
    print(user)

