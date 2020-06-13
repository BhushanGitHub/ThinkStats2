"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

# import nsfg as ng
import thinkstats2
from nsfg import ReadFemResp

from nsfg import ValidatePregnum


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    """
    Exercise 1.2 In the repository you downloaded, you should ﬁnd a ﬁle named chap01ex.py; using this ﬁle as a starting 
    place, write a function that reads the respondent ﬁle, 2002FemResp.dat.gz.
    """
    resp = ReadFemResp(dat_file= "2002FemResp.dat.gz")
    preg = ReadFemResp(dat_file= "2002FemPreg.dat.gz")
    """
    The variable pregnum is a recode that indicates how many times each respondent has been pregnant. 
    Print the value counts for this variable and compare them to the published results in the NSFG codebook.
    """
    print(f'Pregnant Value Count : {resp.pregnum.value_counts()}')

    """
    You can also cross-validate the respondent and pregnancy ﬁles by comparing pregnum for each respondent with 
    the number of records in the pregnancy ﬁle.
    """
    print(ValidatePregnum(resp, preg))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
