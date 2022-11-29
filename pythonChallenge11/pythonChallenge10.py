# Create a function that converts any string  value to a sentence case, then
# write a unit test that check the function's correctness

def proper(sentence):
    words = sentence.split(". ")
    new = ". ".join([word.capitalize() for word in words])
    return new


sentence = "all is going to be fine."
n = proper(sentence)
print(n)