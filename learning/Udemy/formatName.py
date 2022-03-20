def formatName(first,last):
    """This is my sweet Docstring!"""
    name = first.title() + ' ' + last.title()
    return name

name = formatName(input('Enter your first name: '), input('Enter your last name: '))
print(name)
