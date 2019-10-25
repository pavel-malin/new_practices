# Opening two files at once for copying content
with open('file1', 'r') as source:
    with open('file2', 'w') as destination:
        destination.write(source.read())
