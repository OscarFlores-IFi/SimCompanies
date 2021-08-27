# -*- coding: utf-8 -*-


OBL = lambda Sp,Inp,Pw,Pu,Pb,Sk,Ro : ((Sp - Inp) / ((1 - Pb) * Pw * (1 - 0.03 * Ro)) - 1) * 170 / (2 * (1 - Sk))
P = lambda Bl,Sp,Inp,Pw,Pu,Pb,Sk,Ro : (Sp - Inp - Pw * (1 - 0.03 * Ro) * (1 + Bl * (1 - Sk) / 170) * (1 - Pb)) * Bl * Pu / (1 - Pb)*24

Bl,Sp,Inp,Pw,Pu,Pb,Sk,Ro = 70,4900,3720,740,0.84,0.07,0.25,0

OBL_s = OBL(Sp,Inp,Pw,Pu,Pb,Sk,Ro)
P_s = P(OBL_s,Sp,Inp,Pw,Pu,Pb,Sk,Ro)

print(OBL_s, P_s)
