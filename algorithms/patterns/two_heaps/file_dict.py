import json 
def intodict():
    l=[]
    with open('/Users/gunjannividata/demo/c360/two_heaps/dict.txt','r') as file:
        for line in file:
            print(line)
            l.append(json.loads(line))
        print(l)	
intodict()