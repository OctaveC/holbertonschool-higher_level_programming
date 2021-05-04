def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        tupple = len(sentence), sentence[0]
    return tupple
