import numpy as np
import pandas as pd

from src.utils.preprocessor import preprocess_payload
from src.utils.tokenizer import xss_tokenizer, clean_tokenized_payloads
from src.utils.vectorizer import xss_payloads_vectorizer, get_sorted_tokens


def process_payloads(payloads, sorted_tokens=None):
    # Preprocess payloads
    preprocessed_payloads = preprocess_payload(payloads['Payloads'])

    # Tokenize payloads
    tokenized_payloads = [xss_tokenizer(payload) for payload in preprocessed_payloads]

    # Vectorize payloads
    if sorted_tokens is None:
        x_tfidf = xss_payloads_vectorizer(preprocessed_payloads, tokenized_payloads)
        sorted_tokens = get_sorted_tokens(x_tfidf)
        sorted_tokens.append('None')

    cleaned_tokenized_payloads = clean_tokenized_payloads(tokenized_payloads, sorted_tokens)
    return sorted_tokens, cleaned_tokenized_payloads


