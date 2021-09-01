def romanToInt(s: str) -> int:
    
    map = {
        'I': 1,
        'V': 5,
        'X': 10,
        "L": 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    res = 0
    i = 0
    while i<(len(s)):
        
        if i+1<len(s) and map[s[i]]<map[s[i+1]]:
            
            res+= map[s[i+1]] - map[s[i]]
            i+=2
            
            
        else: 
            res+= map[s[i]]
            
            i+=1
            
    return res

print(romanToInt('IX'), romanToInt('CX'),romanToInt('MCX'))