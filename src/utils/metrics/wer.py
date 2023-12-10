from typing import Literal

import jiwer


def wer(hyp, ref, type: Literal["relaxed", "strict"] = "relaxed"):
    """
    Computes the Word Error Rate, defined as the edit distance between the
    two provided sentences after tokenizing to words.
    Arguments:
        hyp (string): space-separated sentence
        ref (string): space-separated sentence
        type (string): type of WER computation. relaxed or strict
    Returns:
        int: the WER
    """
    if type == "relaxed":
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
    elif type == "strict":
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

    wer = jiwer.wer(ref, hyp)

    # Normalize WER
    if wer > 1:
        wer = 1
    return wer


def cer(hyp, ref):
    """
    Computes the Character Error Rate, defined as the edit distance.
    Arguments:
        hyp (string): space-separated sentence
        ref (string): space-separated sentence
    Returns:
        int: the CER
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

    cer = jiwer.cer(
        ref,
        hyp,
        hypothesis_transform=jiwer.remove_empty_strings
    )

    # Normalize CER
    if cer > 1:
        cer = 1
    return cer
