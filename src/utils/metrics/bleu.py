import jiwer


def bleu(hyp: str, ref: str) -> int:
    """
    Computes the BLEU score between a hypothesis and a reference.

    Args:
        hyp: space-separated sentence
        ref: space-separated sentence

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

    bleu = jiwer.bleu(ref, hyp)

    return bleu


def bleu_corpus(hyps: list[str], refs: list[str]) -> int:
    """
    Computes the BLEU score between a corpus of hypotheses and references.

    Args:
        hyps: list of hypotheses
        refs: list of references

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

    bleu = jiwer.bleu(refs, hyps)

    return bleu
