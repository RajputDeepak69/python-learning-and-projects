# we have this library for https connections and methods like get, post etc.
import requests as r

# enter api url of any repo, always better than hard-coding the urls in the code ..
req = input ("enter the api url of any public github repo:")

results = r.get(req)
clear_results = results.json()

# loop chalega tabhi to sbka info aayega 😂
for i in range (len(clear_results)) :
    # this print statement is printing the names of all the pull requesters 
  print (clear_results[i]["user"]["login"])