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

def find_coexistance(D, query): 
    '''(dict,str)->list
    See the assignment text for what this function should do'''

    s=query.split()
        
    for i in range(len(s)):
        s[i]=s[i].replace('-','')
        s[i]=s[i].replace("'",'')
        for ch in string.punctuation:
            s[i]=s[i].strip(ch)
        
    y=D[s[i]]
    for i in range(len(s)-1):
        y = y.intersection(D[s[i+1]])
    y = list(y)
    y.sort()
    return y
    


           
def main():
    file=open_file()
    d=read_file(file)
            # Until input is Q, it will continue to ask for inputs
    while True:
        query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
        if query=='q' or query=='Q':
            break
        try:
            a = find_coexistance(d, query)
        except Exception:
            print("word '"+query+"' not in file.")
        else:
            print('The one or more words you entered coexisted in the following lines of the file:')
            for n in a:
                print(n,end=' ')
            print()
        
    
    
if __name__ == "__main__": #comaparing two functions
    main()
 




