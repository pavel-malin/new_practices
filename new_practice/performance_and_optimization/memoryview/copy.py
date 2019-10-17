@profile
def read_random():
    with open('/dev/urandom', 'rb') as source:
        content = source.read(1024 * 10000)
        content_to_write = content[1024:]
    print("Content lenght: %d, content to writ length %d" %
          (len(content), len(content_to_write)))
    with open('/dev/null', 'wb') as target:
        target.write(content_to_write)


if __name__ == '__main__':
    read_random()
