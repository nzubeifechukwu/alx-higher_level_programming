#!/usr/bin/python3
'''Prints a text

    Add two new lines after each of these characters: <.>, <?>, <:>

'''


def text_indentation(text):
    '''Prints a text with two new lines after any of these characters: . ? :

        Args:
            text: string to print

        Raises:
            TypeError: if text not a string
    '''
    if type(text) is not str:
        raise TypeError('text must be a string')

    new_text = ''

    for c in text:
        if c == '.' or c == '?' or c == ':':
            new_text = new_text + '{}\n\n'.format(c)
        else:
            new_text = new_text + c

    new_text_list = new_text.split('\n\n')

    for t in new_text_list:
        if t[len(t)-1] == '.' or t[len(t)-1] == '?' or t[len(t)-1] == ':':
            print('{}\n\n'.format(t.strip()), end='')
        else:
            print(t.strip(), end='')
