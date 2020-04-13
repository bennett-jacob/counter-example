# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 23:12:29 2018

@author: Bill
"""

import re as regexpr
import numpy


def prepoc(xo: [str]) -> [str]:
    x = []

    # file containing words/characters to remove
    fpnswapstr = "./list-swapstrs.txt"
    with open(fpnswapstr) as fid:
        swapstrs = fid.read().splitlines()
        # ['Garbage', 'Doe']

    # preprocess strings by indication
    for jjx in range(len(xo)):
        # [0, 1, 2, 3, 4]

        # have to cast to list bc is numpy.ndarray
        # NOTE: The input file in text_load.py was a csv. We decided to return
        # the numpy.ndarray and we now have to transform it.
        # A better way is to do the data transformation within the `load()`
        # function in text_load.py.
        # line = list(xo[jjx])
        # tstr = " ".join(line).lower()

        # Other implementation
        # xo is a list of strings
        tstr = xo[jjx].lower()

        for swapstr in swapstrs:
            tstr = regexpr.sub(swapstr, " ", tstr)

        tstr = tstr.split(" ")
        # "This is a sentence" -> ["This", "is", "a", "sentence"]

        for tword in tstr:
            # only inlude words we want
            if len(tword) > 1:
                # this removes non-alphanumeric characters from string
                # https://stackoverflow.com/a/1276774/5623385
                tword = regexpr.sub(r"\W+", "", tword)
                x.append(tword)

    return x

    # code after "return" doesn't get executed
    del tstr, jjx, tword
    del fpnswapstr, swapstrs, swapstr
    # del clv0 clv1


#
