# Hello World program in Python

import itertools

def perm(seq, n):
    return itertools.product(seq, repeat=n)

def neighborhood(genome, d):
    return [''.join(g) for g in perm('ACGT', len(genome)) if hamming(''.join(g), genome) <= d]

def get_k_mer(sequence, k):
    for i in range(len(sequence) - k+1):
        yield sequence[i:i + k]

def count_pattern(genome, strand, diff):
    return len([kmer for kmer in get_k_mer(genome, len(strand)) if hamming(kmer, strand) <= diff])

def skew(strand):
    skew = [0]
    counter = 0
    for s in strand:
        if 'C' == s:
            counter -= 1
        if 'G' == s:
            counter += 1
        skew.append(counter)
    return skew
    
def min_skew(skew):
    return skew.index(min(skew))
    
def max_skew(skew):
    return skew.index(max(skew))

def hamming(str1, str2):
    return sum(1 for s1, s2 in zip(str1, str2) if s1 != s2)


print hamming("TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC", "GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA")
# print ' '.join(map(str,skew('GAGCCACCGCGATA')))
# print min_skew(skew('CATTCCAGTACTTCGATGATGGCGTGAAGA'))
# print max_skew(skew('CATTCCAGTACTTCATGATGGCGTGAAGA'))
# print count_pattern('CGTGACAGTGTATGGGCATCTTT','TGT', 1)
# print perm('ACGT',2)
# print len(neighborhood('CCAGTCAATG',1))