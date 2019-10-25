# Opening two files at once with a with statement
with open('file1', 'r') as source, open('file2', 'w') as destination:
    destination.write(source.read())
