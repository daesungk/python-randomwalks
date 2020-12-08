import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def RW1D(Pr, NumSteps, Up, Down):
    Sample = np.random.random(NumSteps)
    Inc = np.full(NumSteps, 0)
    RW = np.full(NumSteps, 0)
    for i in range(NumSteps):
        if Sample[i] >= Pr:
            Inc[i] = Up
        else:
            Inc[i] = Down
    for j in range(NumSteps):
        if j == 0:
            RW[j] = 0
        else:
            RW[j] = RW[j-1] + Inc[j]
    return RW

def SRW1D(N):
    return RW1D(0.5,N,1,-1)

def NRW1D(Pr, NumSteps, Up, Down):
    Mean = Up * (1-Pr) + Down * Pr
    Var = (Up**2) * (1-Pr) + (Down**2) * Pr - Mean**2
    RW = RW1D(Pr, NumSteps, Up, Down)
    NRW = np.full(NumSteps, 0)
    for i in range(NumSteps-1):
        NRW[i+1] = (RW[i+1]-(i+1)*Mean)/(np.sqrt((i+1)*Var))
    return NRW

def NSRW1D(N):
    return NRW1D(0.5,N,1,-1)


def Hitting(NumSteps, Upbd, Lowbd):
    RW = SRW1D(NumSteps)
    for i in range(NumSteps):
        if RW[i] >= Upbd or RW[i]<= Lowbd:
            return i
            break
        else:
            return "Infinity"


