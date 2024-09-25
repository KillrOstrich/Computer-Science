#Decleration - create
#Assignment - modify
FA = input("what is your favorite animal?") # Qestion determines Favorite Animal/FA
print("your Fav animal is " + FA +"!") # statment uses FA to test and conferm
REA = input("why is your Fav animal " + FA + "?") # Qestion determines 1st reason/REA
print(REA + " is an interesting reason.") # test/conferm
sub = input("is it a sub species or just the speices as a whole?") # brings more specifics on FA aka subspecies/sub
print("so " + sub + ", good pick!") # test/conferm
rea = input("is there another reason you like them?") # qestion determines reason2/rea
print(rea + ", interesting") # test/conferm
FIN = input("is there any interesting facts about " + FA + "'s?")
print("so your Fav animal is a " + FA + " your reason is " + REA + ". you mainly like " + sub + " because " + rea + ". an interesting fact is " + FIN + ".")