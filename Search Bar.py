import string

def open_file():
    '''None->file object'''
   
    while True:
        try:
            # entering filename
            t = input("Enter filename: ")
        #exceptions will be passed
            t = t.strip()
            fp = open(t)
        except Exception:
            print ('There is no file with that name. Try again.')
            # looping until correct filename is inserted
        else:
            return fp
   

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
 
    f = fp.read().lower().splitlines()
    
    for i in range(len(f)):
        for ch in set(string.punctuation):
            f[i]=f[i].replace(ch,'')
            
        f[i] = f[i].split()
    dic={}
    
    for l in range(len(f)):
        for w in range(len(f[l])):
            f[l][w].replace("'",'')
            f[l][w].replace('-','')
            if f[l][w].isalpha() and len(f[l][w])>=2:
                if f[l][w] in dic:
                    dic[f[l][w]].add(l+1)
                else:
                    dic[f[l][w]]={l+1}
    return dic



           

        
    
    





