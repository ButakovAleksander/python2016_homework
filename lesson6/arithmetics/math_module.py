# -*- coding: utf-8-*-

import numpy as np


def convert_to_array(lst):

    return np.array(lst).astype(float)


def do_sum(array):

    vector_sum = array.sum()

    return vector_sum


def do_mean(array):

    vector_mean = array.mean()

    return vector_mean

