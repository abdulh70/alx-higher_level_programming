def multiple_returns(sentence):
    tuplle = ()
    if len(sentence) == 0:
        tuplle = 0, "None"
    else:
        tuplle = len(sentence), sentence[0]
    return tuplle

