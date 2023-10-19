

def get_count(sentence):
    count=0
    vowels='aeiou'
    for i in sentence:
        for j in vowels:
            if i==j:
                count=count+1
    
    return count


"""
sentence='asdfas'

output:2

"""
