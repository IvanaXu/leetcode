BASH = """
# Read from the file file.txt and print its transposed content to stdout.
python3 << end
_r = []
with open('file.txt', 'r') as f:
    for i in f:
        i = i.rstrip('\n').split()
        _r.append(i)
for i in zip(*_r):
    print(' '.join(i))
end
"""
