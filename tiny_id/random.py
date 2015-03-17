# standard libraries
pass
# third party libraries
import numpy
# podimetrics libraries
pass

# define the corpus as alphanumeric, url-safe characters that are 
# unlikely to be mistaken for each other
_CORPUS = list("23456789"
               "ABCDEFGHJKLMNPQRSTUVWXYZ"
               "abcdefghijkmnopqrstuvwxyz")

def collision_likelihood(length):
    pass

def bits_to_length(n):
    base = len(_CORPUS)
    length = int(bits/numpy.log2(base) + 0.5)
    return length

def generate(length=22):
    """
    length = 22 corresponds to > 128 bits of entropy (comparable to uuid)

    if you wanted bits instead

    the birthday paradox can be used to estimate probability of collision 
    Pr ~= 1 - exp(-n**2/(2*d))

    where n is the number of random ids generated, and d = 2**bits
    """
    random_string, = numpy.random.choice(_CORPUS, length).view('S' + str(length))
    return random_string