
data  = 'aaaabbbccajjjjafffrrrwww'

def encode(data):
    encoding = ""
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + data[i]
        i = i + 1
    return encoding

RLE_code = encode(data)

print(RLE_code)

def full_code(code):
    full_str = ''
    for e in range(0,len(code)):
        if e % 2 == 0:
            full_str =  full_str + int(code[e]) * code[e+1]
    return full_str
    
print(full_code(RLE_code))  
        