# Convert to string
string_1 = str(1)
string_2 = str(4.5)
string_3 = str(True)

print([string_1, string_2, string_3])

#Escape Sequence
print('string\'s')

#Raw String
path = r'C:\User\Pragatheesh\Desktop'
print(path)

#Slicing and Indexing
my_string = "Ironman"

index1 = my_string[0]
slice1 = my_string[0:4]
slice2 = my_string[4:]

print(index1)
print(slice1)
print(slice2)

#Length
my_string = 'Ironman'
my_length = len(my_string)

print(my_length)

#Case
my_string = "Ironman"

uppercase = my_string.upper()
lowercase = my_string.lower()
title = my_string.title()

print(uppercase)
print(lowercase)
print(title)

#Reverse
my_hero = "Ironman"
my_oreh = my_hero[::-1]

print(my_oreh)

#Find
my_string = "where\'s westview"
there = my_string.find('westview')

print(my_string)
print(there)

#count
my_string = "where\'s westview"
there = my_string.count('w')

print(my_string)
print(there)

#Replace
my_string = "where\'s westview"
there = my_string.replace('w','t',1)

print(my_string)
print(there)

#Add
str1 = "I"
str2 = "am"
str3 = "Ironman"

replay_to_thanos = str1 + ' ' + str2 + ' ' + str3

print(replay_to_thanos)

#Join
words = ["I", "am", "Ironman"]
tony_stark = " ".join(words)

print(tony_stark)

#Split
tony_stark = "I am Ironman"
words = tony_stark.split( ' ', 1)

print(words)

#R-Split
tony_stark = "I am Ironman"
words = tony_stark.rsplit(' ', 1)

print(words)

#Strip
tony_stark = "     I am Ironman  "

clean = tony_stark.strip()
rclean = tony_stark.rstrip()
lclean = tony_stark.lstrip()

print(tony_stark)
print(clean)
print(rclean)
print(lclean)

#F-String
from datetime import datetime

my_today = datetime.now()

print(f"Today's date is {my_today:%B %d, %Y}")

#Positional Formatting
x = 'friendly'
y = 'spiderman'

peter_parker = 'I am your {} neighbourhood {}'.format(x,y)

print(peter_parker)

#Regular Expressions
import re
string = '789xyz'
regex = True if re.search (r'[a-z]+', string) else false

print(regex)