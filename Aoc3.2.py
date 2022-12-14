def find_in_string(x ,y, z):
    for c in x:
        if y.count(c) > 0:
           if z.count(c) > 0:
                return c
    
#base set asci leters with values being index + 1
import string
import linecache
priorities = list(string.ascii_letters)
found=[]
final = 0
holder=[]

# open the sample file used
file = open('Day3/input')
  
# read the content of the file opened
content = file.readlines()
i=0
q=0
while i < len(content) +1:
    if (q % 3) == 0 and q != 0:
        q=0
        found.append(find_in_string(holder[0],holder[1],holder[2]))
        holder.clear()
    if i <len(content):
        holder.append(content[i].rstrip("\n")) 
    q+=1
    i+=1
    
    

    
#
for c in found:
    final += priorities.index(c) + 1
print(final)

