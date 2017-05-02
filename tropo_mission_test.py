
say("Hello, welcome to the language selector version 7")
result = ask("please press 1 for French, 2 for Italian, 0 for english", {
   "choices": "[1 DIGITS]",
   "terminator": "#",
   "mode": "dtmf"})

log("the language of your choice:" + result.value)
say("you chose " + result.value)
if int(result.value) == 0: 
   say("Hello my friend", {voice: "Karen"})
elif int(result.value) == 1:
   say("Bonjour mon ami", {voice: "Aurelie"})
elif int(result.value) == 2:
   say("Bongiorno Principe", {voice: "Federica"})
else:
   hangup()

hangup()