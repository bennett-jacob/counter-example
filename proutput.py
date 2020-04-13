# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 20:45:17 2018

@author: Bill
"""


def output(xo, wc):
    numind = 50
    nprcol = 20
    fpnout = "./ct4pe-common-inds.csv"
    fidout = open(fpnout, "w")

    print("\nTop {0:d} Order Indication Words".format(numind))
    print("--------")
    print("Indication,#Ordered", file=fidout)
    print("Total # Orders = {0:d}".format(len(xo)), file=fidout)

    print("==================")

    for jji in range(min(numind, len(wc))):
        padto = nprcol - len(wc[jji][0])
        if jji % 2 == 0:
            padstr = "."
        else:
            padstr = " "
        print("{0:4d}: ".format(jji + 1), end="")
        print(wc[jji][0] + ":" + padstr * padto + str(wc[jji][1]))
        print("{0:s},{1:d}".format(wc[jji][0], wc[jji][1]), file=fidout)

    fidout.close()

    #
