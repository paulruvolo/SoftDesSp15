class DNASequence:
    """ Represents a sequence of DNA """
    def __init__(self, nucleotides):
        """ constructs a DNASequence with the specified nucleotides.
             nucleotides: the nucleotides represented as a string of
                          capital letters in {'A','C','G','T'} """
        self.nucleotides = nucleotides
        
    def get_reverse_complement(self):
        """ Computes the reverse complement of the DNA sequence.
            returns: the reverse complement DNA sequence represented
                     as an object of type DNASequence

            >>> seq = DNASequence("ATGC")
            >>> print seq.get_reverse_complement()
            GCAT
        """
        ret_list = []
        complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
        for n in reversed(self.nucleotides):
            ret_list.append(complement[n])
        return DNASequence(''.join(ret_list))

    def __str__(self):
        """ Returns a string containing the nucleotides in the DNASequence
        >>> seq = DNASequence("TTTGCC")
        >>> print seq
        TTTGCC
        """
        return self.nucleotides

    def get_proportion_ACGT(self):
        """ Computes the proportion of nucleotides in the DNA sequence
            that are 'A', 'C', 'G', and 'T'
            returns: a dictionary where each key is a nucleotide and the
                corresponding value is the proportion of nucleotides in the
            DNA sequence that are that nucleotide.
            (NOTE: this doctest will not necessarily always pass due to key
                    re-ordering don't worry about matching the order)
        >>> seq = DNASequence("AAGAGCGCTA")
        >>> d = seq.get_proportion_ACGT()
        >>> print (d['A'], d['C'], d['G'], d['T'])
        (0.4, 0.2, 0.3, 0.1)
        """
        l = float(len(self.nucleotides))
        return {'A': self.nucleotides.count('A')/l,
                'C': self.nucleotides.count('C')/l,
                'G': self.nucleotides.count('G')/l,
                'T': self.nucleotides.count('T')/l}

if __name__ == '__main__':
    import doctest
    doctest.testmod()