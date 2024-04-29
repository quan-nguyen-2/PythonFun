def titleize(phrase):

    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    new_word = ''
    new_lst = phrase.split()
    for i in new_lst:
        if i(i.index() - 1) == " ":
            new_word.append(i.upper())
    return new_word
