# coding=utf-8
import numpy as np
from math import *


def calc(M):

    beta = np.linspace(0, pi / 2, 1000)
    # print M
    temp1 = np.multiply(M, M)
    temp2 = np.multiply(np.sin(beta), np.sin(beta))
    temp3 = np.multiply(temp1, temp2) - 1
    # print temp3
    temp2 = 1.4 + np.cos(2 * beta)
    temp4 = np.multiply(temp1, temp2) + 2
    # print temp4
    temp5 = np.divide(temp3, temp4)
    temp6 = np.multiply(2 / np.tan(beta), temp5)
    theta = np.arctan(temp6)
    # print theta
    # temp7 = theta < 0
    beta = np.round(beta / pi * 180, 1)
    theta = np.round(theta / pi * 180, 1)
    # theta[temp7] = 0

    return [theta, beta]


if __name__ == '__main__':
    [theta, beta] = calc(2)
    print theta
