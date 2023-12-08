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
