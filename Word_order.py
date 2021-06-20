# Enter your code here. Read input from STDIN. Print output to STDOUT
vocab = {}

for i in range(int(input())):
    value = input()
    if not vocab.get(value, None):
        vocab[value] = 1
    else:
        vocab[value] += 1
        
print(len(vocab));
print(*vocab.values())
    
     