# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 13:34:23 2018

@author: u6014379
"""

from collections import Counter
from operator import itemgetter


def counter(x: [str]):
    wc = Counter(x)  # counts words, counter object
    wc = dict(wc)  # convert to standard dictionary

    # sort by frequency of word to list
    wc = sorted(wc.items(), key=itemgetter(1), reverse=True)

    return wc

    # del wc

    #
