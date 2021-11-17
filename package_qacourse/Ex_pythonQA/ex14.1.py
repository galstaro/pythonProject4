story=open('story.txt','w')
story.write("A boy is playing there.\n")
story.write("There is a play ground.\n")
story.write("An airplane is in the sky.\n")
story.write("The sky is pink.\n")
story.write("Alphabets and numbers are allowed in the password.\n")
story.close()
storyread=open('story.txt','r')
print(storyread.read())
storyread.close()
storyread=open('story.txt','r')
count=0
for line in storyread:
    if line[0]!="T":
        count+=1
storyread.close()
print(count)
storyread=open('story.txt','r')
count=0
for line in storyread:
    lis=line.split()
    print(lis)
    for i in lis:
        if i=="The" or i=="the":
            count+=1
storyread.close()
print(count)

with open('story.txt','r') as story:
    print(story.read().strip())

with open('story.txt','r') as story:
    print(len(list(story)))