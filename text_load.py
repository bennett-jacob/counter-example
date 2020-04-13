# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 23:12:29 2018

@author: Bill
"""
import numpy as np

# Interactive File Dialogue Menu
# in_path = filedialog.askopenfilename()

# home
# fpndat = 'C:/Users/Bill/Dropbox/1Wrk/Informatics/Cds-auc/ct-all-indications-freetext.txt'

# work


def load() -> [str]:
    fpndat = "/Users/jacobbennett/Documents/projects/andy/first/120-0.txt"
    lines = []

    # load file and delete '\n' characters
    with open(fpndat) as fid:
        # ========================
        # Implementation 1
        # Expects csv
        # ========================
        # # This is fragile. It breaks if the csv file is poorly formatted, or if
        # # you use a non-csv file
        # xo = np.genfromtxt(fpndat, dtype="str", delimiter=",")
        # print(xo)

        # # take list of strings and make it one string
        # for i in xo:
        #     lines.append(" ".join(i))

        # ========================
        # Implementation 2
        # Takes anything
        # ========================
        xo = fid.read().splitlines()
        for i in range(len(xo)):
            lines.append(xo[i])

    return lines
