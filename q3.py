# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

####
#### YOUR CODE HERE 
####
count=0
with open("romeo_and_juliet.txt", "r") as f:
    text= f.read()

# # Count how many times the word "Juliet" appears

#look at every word in text
for word in text.split(" "):

# for "Juliet" in text:
# if the word is juliet or Juliet (i.e. if text.lower() is "juliet"), then increment the count by 1
        if "juliet" in word.lower():  
            count += 1
print(count)

