# Input:  "programming"
# Output: 'p'

def first_non_repeating_char(txt):
    f={}
    for i in txt:
        f[i]=f.get(i,0)+1
    for key in f.keys():
        if f[key]==1:
            return key
    
result=first_non_repeating_char('programming')
print(result)