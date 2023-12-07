import jiwer


def wer(hyp, ref):
    """
    Computes the Word Error Rate, defined as the edit distance between the
    two provided sentences after tokenizing to words.
    Arguments:
        hyp (string): space-separated sentence
        ref (string): space-separated sentence
    """
    return jiwer.wer(ref, hyp)
