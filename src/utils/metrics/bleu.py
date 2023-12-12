import jiwer


def bleu(hyp, ref):
    """
    Computes the BLEU score between a hypothesis and a reference.
    Arguments:
        hyp (string): space-separated sentence
        ref (string): space-separated sentence
    Returns:
        int: the BLEU score
    """
    transform = jiwer.Compose(
        [
            jiwer.ToLowerCase(),
            jiwer.RemoveMultipleSpaces(),
            jiwer.RemoveWhiteSpace(replace_by_space=True),
            jiwer.RemovePunctuation(),
            jiwer.Strip(),
            jiwer.SentencesToListOfWords(word_delimiter=" "),
        ]
    )

    hyp = transform(hyp)
    ref = transform(ref)

    bleu = jiwer.sentence_bleu(ref, hyp)

    return bleu


def bleu_corpus(hyps, refs):
    """
    Computes the BLEU score between a corpus of hypotheses and references.
    Arguments:
        hyps (list): list of hypotheses
        refs (list): list of references
    Returns:
        int: the BLEU score
    """
    transform = jiwer.Compose(
        [
            jiwer.ToLowerCase(),
            jiwer.RemoveMultipleSpaces(),
            jiwer.RemoveWhiteSpace(replace_by_space=True),
            jiwer.RemovePunctuation(),
            jiwer.Strip(),
            jiwer.SentencesToListOfWords(word_delimiter=" "),
        ]
    )

    hyps = [transform(hyp) for hyp in hyps]
    refs = [transform(ref) for ref in refs]

    bleu = jiwer.corpus_bleu(refs, hyps)

    return bleu
