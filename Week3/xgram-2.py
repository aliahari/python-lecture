users = ["Alice", "Bob"]
postsAlice = ["Wow! Iam finally in Karlsruhe!", "Great music @ AKK"]
postsBob = ["Great time at python class!"]
imgsAlice = ["shorturl.at/chDUX", "shorturl.at/aorP1"]
imgsBob =["shorturl.at/wxFLR"]
postsBob.append("I just learned about lists!") #add a new post 
oldPostsAlice = ["Got the ticket", "On my way to Karlsruhe"]
postsAlice = oldPostsAlice + postsAlice #add oldPostsAlice to the beginning of postsAlice
#print(postsAlice[-2:]) #print last two posts

xgramPost = {"Alice":[("Wow! Iam finally in Karlsruhe!","shorturl.at/chDUX"), ( "Great music @ AKK","shorturl.at/aorP1")], "Bob":[("Great time at python class!","shorturl.at/wxFLR"),("I just learned about lists!","")]}

print(xgramPost["Alice"][-1][1]) 



