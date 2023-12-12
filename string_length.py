
def string(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]


print(string('ruta desai'))
print(string('rd'))
print(string('r'))
