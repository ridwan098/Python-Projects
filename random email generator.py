import random


from datetime import datetime


now = datetime.now()


num=random.randint(0,9999)


ng1=["terrible","tom","123","12","deadly","usa","russian","python","gamer","42","work","youtube","girl","boy","man","book","sports","fox","wolf","coffee","abc","killer","academy","1995","2004",num,"walmart","sucks","duck","gf","bf",now.year,"gif","friendly","scott","south","north","east","west","side","dude","yolo","brick","code","monkey","apple","linux","windows","android","ios","password","random","hockey","qwerty","asdf","plm","mom","dad","mother","father","kid","rock","giant","music","date","addiction","christian","atheist","god","jesus","muhammad","freak","fresh","hardcore","history","buff","happy","sad","pacifist","sandwich","griffin","waifu","anime","gb","college","school","money","google","professional","john","taking","running","communist","supporter","gun","fart","lgfhdhsg","withclass","ad","admin","art","420","cactus","soccer","football","dog","cat","ocean","sarah","cute","gtfo","lol","f","online","wwyd","hitmeup","talking","email","mail","jump","smith","starwars","corporate","pizza","hot","sexy","pvcs","stolen","thief","food","tab","assassin","salesman","propane","lipstick","makeup","fghjk","tgbvc","magic","death","love","robot","bot","trump","crazy","lonely","ahri","senpai","internet","web","phone","dgigd","who","ted","earnie","secure","stecri"]


listnum=len(ng1)-1


x=random.randint(0,listnum)


y=random.randint(0,listnum)


z=random.randint(0,9)


w=random.randint(0,3)


at=["gmail","hotmail","live","outlook","yahoo","mail","aol","inbox","zoho","gmail"]


if w == 0:


 print (ng1[x],ng1[y],"@",at[z],".com",sep="")


if w == 1:


 print (num,ng1[x],ng1[y],"@",at[z],".com",sep="")


if w == 2:


 print (ng1[x],ng1[y],num,"@",at[z],".com",sep="")


if w == 3:


 print (ng1[x],num,ng1[y],"@",at[z],".com",sep="")


 


#sorry if it happens to be a real email lol


#feel free to add words
