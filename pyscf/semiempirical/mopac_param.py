#
# Modified based on MINDO3_Parameters.py and Slater.py in PyQuante-1.6
#
"""
 MINDO3.py: Dewar's MINDO/3 Semiempirical Method

 This program is part of the PyQuante quantum chemistry program suite.

 Copyright (c) 2004, Richard P. Muller. All Rights Reserved.

 PyQuante version 1.2 and later is covered by the modified BSD
 license. Please see the file LICENSE that is part of this
 distribution.
"""

import numpy
from pyscf import lib
from pyscf.data.nist import HARTREE2EV

E2 = 14.399             # Coulomb's law coeff if R in \AA and resulting E in eV
E2 /= HARTREE2EV        # Convert to Hartree
EV2KCAL = 23.061        # Conversion of energy in eV to energy in kcal/mol
HARTREE2KCAL = HARTREE2EV * EV2KCAL

#############################
#
# MINDO/3 parameters
#

# in eV
USS3 = numpy.array((
        0.  , -12.505, 0.  ,
        0.  , 0.  , -33.61, -51.79, -66.06, -91.73, -129.86, 0.  ,
        0.  , 0.  , 0.    , -39.82, -56.23, -73.39, -98.99 , 0.  ,
))
UPP3 = numpy.array((
        0.  , 0.  , 0.  ,
        0.  , 0.  , -25.11, -39.18, -56.40, -78.80, -105.93, 0.  ,
        0.  , 0.  , 0.    , -29.15, -42.31, -57.25, -76.43 , 0.  ,
))
# Convert to Eh
USS3 *= 1./HARTREE2EV
UPP3 *= 1./HARTREE2EV

# *** ONE CENTER REPULSION INTEGRALS
#     GSS ::= (SS,SS)
#     GPP ::= (PP,PP)
#     GSP ::= (SS,PP)
#     GP2 ::= (PP,P*P*)
#     HSP ::= (SP,SP)
GSSM = numpy.array((
        0.  , 12.848, 0.  ,
        0.  , 9.00, 10.59, 12.23, 13.59, 15.42, 16.92, 0.  ,
        0.  , 0.  , 8.09, 9.82, 11.56, 12.88, 15.03, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
                    0.  , 0.  , 0.  , 0.  , 15.03643948, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
                    0.  , 0.  , 0.  , 0.  , 15.04044855, 0.  ,
))
GPPM = numpy.array((
        0.  , 0.  , 0.  ,
        0.  , 6.97, 8.86, 11.08, 12.98, 14.52, 16.71, 0.  ,
        0.  , 0.  , 5.98, 7.31, 8.64, 9.90, 11.30, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
                    0.  , 0.  , 0.  , 0.  , 11.27632539, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
                    0.  , 0.  , 0.  , 0.  , 11.14778369, 0.  ,
))
GSPM = numpy.array((
        0.  , 0.  , 0.  ,
        0.  , 7.43, 9.56, 11.47, 12.66, 14.48, 17.25, 0.  ,
        0.  , 0.  , 6.63, 8.36, 10.08, 11.26, 13.16, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
                    0.  , 0.  , 0.  , 0.  , 13.03468242, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
                    0.  , 0.  , 0.  , 0.  , 13.05655798, 0.  ,
))
GP2M = numpy.array((
        0.  , 0.  , 0.  ,
        0.  , 6.22, 7.86, 9.84, 11.59, 12.98, 14.91, 0.  ,
        0.  , 0.  , 5.40, 6.54, 7.68, 8.83, 9.97, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
                    0.  , 0.  , 0.  , 0.  , 9.85442552, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
                    0.  , 0.  , 0.  , 0.  , 9.91409071, 0.  ,
))
HSPM = numpy.array((
        0.  , 0.  , 0.  ,
        0.  , 1.28, 1.81, 2.43, 3.14, 3.94, 4.83, 0.  ,
        0.  , 0.  , 0.70, 1.32, 1.92, 2.26, 2.42, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
                    0.  , 0.  , 0.  , 0.  , 2.45586832, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
                    0.  , 0.  , 0.  , 0.  , 2.45638202, 0.  ,
))
HP2M = numpy.array((
        0.  , 0.  , 0.  ,
        0.  , 0.  , 0.50, 0.62, 0.70, 0.77, 0.90, 0.  ,
        0.  , 0.  , 0.  , 0.38, 0.48, 0.54, 0.67, 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
        0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
))
GSSM *= 1./HARTREE2EV
GPPM *= 1./HARTREE2EV
GSPM *= 1./HARTREE2EV
GP2M *= 1./HARTREE2EV
HSPM *= 1./HARTREE2EV
HP2M *= 1./HARTREE2EV


# *** F03 IS THE ONE CENTER AVERAGED REPULSION INTEGRAL FOR USE IN THE
#        TWO CENTER ELECTRONIC REPULSION INTEGRAL EVALUATION.
F03 = numpy.array((
        0., 12.848, 10.0,
        10.0, 0.0, 8.958, 10.833, 12.377, 13.985, 16.250,
        10.000, 10.000, 0.000, 0.000,7.57 ,  9.00 ,10.20 , 11.73
))
F03 *= 1./HARTREE2EV

VS = numpy.array((
        0.  , -13.605, 0.  ,
        0.  , 0.  , -15.160, -21.340, -27.510, -35.300, -43.700, -17.820,
        0.  , 0.  , 0.     , 0.     , -21.100, -23.840, -25.260, 0.     ,
))
VP = numpy.array((
        0.  , 0.  , 0.  ,
        0.  , 0.  , -8.520, -11.540, -14.340, -17.910, -20.890, -8.510,
        0.  , 0.  , 0.    , 0.     , -10.290, -12.410, -15.090, 0.    ,
))
VS *= 1./HARTREE2EV
VP *= 1./HARTREE2EV

# *** HERE COMES THE OPTIMIZED SLATER_S EXPONENTS FOR THE EVALUATION
#     OF THE OVERLAP INTEGRALS AND MOLECULAR DIPOLE MOMENTS.
ZS3 = numpy.array((
        0.  , 1.30, 0.  ,
        0.  , 0.  , 1.211156, 1.739391, 2.704546, 3.640575, 3.111270, 0.  ,
        0.  , 0.  , 0.      , 1.629173, 1.926108, 1.719480, 3.430887, 0.  ,
))
ZP3 = numpy.array((
        0.  , 0.  , 0.  ,
        0.  , 0.  , 0.972826, 1.709645, 1.870839, 2.168448, 1.419860, 0.  ,
        0.  , 0.  , 0.      , 1.381721, 1.590665, 1.403205, 1.627017, 0.  ,
))


# *** BETA3 AND ALP3 ARE THE BOND PARAMETERS USED IN THE
#     RESONANCE INTEGRAL AND THE CORE CORE REPULSION INTEGRAL RESPECTIVE
Bxy = numpy.array((
        # H                B         C         N         O         F                     Si        P         S        Cl
        0.244770,
        0       , 0,
        0       , 0, 0,
        0       , 0, 0, 0,
        0.185347, 0, 0, 0, 0.151324,
        0.315011, 0, 0, 0, 0.250031, 0.419907,
        0.360776, 0, 0, 0, 0.310959, 0.410886, 0.377342,
        0.417759, 0, 0, 0, 0.349745, 0.464514, 0.458110, 0.659407,
        0.195242, 0, 0, 0, 0.219591, 0.247494, 0.205347, 0.334044, 0.197464,
        0       , 0, 0, 0, 0       , 0       , 0       , 0       , 0       , 0,
        0       , 0, 0, 0, 0       , 0       , 0       , 0       , 0       , 0, 0,
        0       , 0, 0, 0, 0       , 0       , 0       , 0       , 0       , 0, 0, 0,
        0       , 0, 0, 0, 0       , 0       , 0       , 0       , 0       , 0, 0, 0, 0,
        0.289647, 0, 0, 0, 0       , 0.411377, 0       , 0       , 0       , 0, 0, 0, 0, 0.291703,
        0.320118, 0, 0, 0, 0       , 0.457816, 0       , 0.470000, 0.300000, 0, 0, 0, 0, 0       , 0.311790,
        0.220654, 0, 0, 0, 0       , 0.284620, 0.313170, 0.422890, 0       , 0, 0, 0, 0, 0       , 0       , 0.202489,
        0.231653, 0, 0, 0, 0       , 0.315480, 0.302298, 0       , 0       , 0, 0, 0, 0, 0       , 0.277322, 0.221764, 0.258969,
))
BETA3 = lib.unpack_tril(Bxy)
del(Bxy)

Axy = numpy.array((
        # H                B         C         N         O         F                     Si        P         S        Cl
        1.489450,
        0       , 0,
        0       , 0, 0,
        0       , 0, 0, 0,
        2.090352, 0, 0, 0, 2.280544,
        1.475836, 0, 0, 0, 2.138291, 1.371208,
        0.589380, 0, 0, 0, 1.909763, 1.635259, 2.029618,
        0.478901, 0, 0, 0, 2.484827, 1.820975, 1.873859, 1.537190,
        3.771362, 0, 0, 0, 2.862183, 2.725913, 2.861667, 2.266949, 3.864997,
        0       , 0, 0, 0, 0       , 0       , 0       , 0       , 0       , 0,
        0       , 0, 0, 0, 0       , 0       , 0       , 0       , 0       , 0, 0,
        0       , 0, 0, 0, 0       , 0       , 0       , 0       , 0       , 0, 0, 0,
        0       , 0, 0, 0, 0       , 0       , 0       , 0       , 0       , 0, 0, 0, 0,
        0.940789, 0, 0, 0, 0       , 1.101382, 0       , 0       , 0       , 0, 0, 0, 0, 0.918432,
        0.923170, 0, 0, 0, 0       , 1.029693, 0       , 1.662500, 1.750000, 0, 0, 0, 0, 0       , 1.186652,
        1.700698, 0, 0, 0, 0       , 1.761370, 1.878176, 2.077240, 0       , 0, 0, 0, 0, 0       , 0       , 1.751617,
        2.089404, 0, 0, 0, 0       , 1.676222, 1.817064, 0       , 0       , 0, 0, 0, 0, 0       , 1.543720, 1.950318, 1.792125,
))
ALP3 = lib.unpack_tril(Axy)
del(Axy)


# *** EISOL3 AND EHEAT3 ARE THE GS ELECTRONIC ENERGY OF THE NEUTRAL ATOM
#     (IN E.V.) AND THE HEAT OF FORMATION IF THE FREE ATOM (IN KCAL/MOL)
EHEAT3 = numpy.array((
        0.  , 52.102, 0.  ,
        0.  , 0.  , 135.7, 170.89, 113.0, 59.559, 18.86, 0.  ,
        0.  , 0.  , 0.   , 106.0 , 79.8 , 65.65 , 28.95, 0.  ,
))
EISOL3 = numpy.array((
        0.  , -12.505, 0.  ,
        0.  , 0.  ,-61.70,-119.47,-187.51,-307.07,-475.00,0.  ,
        0.  , 0.  , 0.   ,-90.98 ,-150.81,-229.15,-345.93,0.  ,
))

#   CORE IS THE CHARGE ON THE ATOM AS SEEN BY THE ELECTRONS
#
CORE = numpy.array((0,
        1, 0,
        1, 2, 3, 4, 5, 6, 7, 0,
        1, 2, 3, 4, 5, 6, 7, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 2, 3, 4, 5, 6, 7, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 2, 3, 4, 5, 6, 7, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,
           3, 4, 5, 6, 7, 8, 9,10,11, 2, 3, 4, 5, 6, 7, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, -2, -1, 0
))

# MINDO/3 parameters end
##############################
#
# MNDO-PM3 parameters end
#
#      COMMON /PM3 /  USSPM3(107), UPPPM3(107), UDDPM3(107), ZSPM3(107),
#      ZPPM3(107), ZDPM3(107), BETASP(107), BETAPP(107), BETADP(107),
#      ALPPM3(107), EISOLP(107), DDPM3(107), QQPM3(107), AMPM3(107),
#      ADPM3(107), AQPM3(107) ,GSSPM3(107), GSPPM3(107), GPPPM3(107),
#      GP2PM3(107), HSPPM3(107),POLVOP(107)


# MNDO-PM3 parameters end
##############################

# Gaussian functions for fitting to Slaters. These functions are
# STO-6G fits to slater exponents with exponents of 1. To fit
# to exponents of \zeta, you need only multiply each
# exponent by \zeta^2
# The rest of these functions can be obtained from Stewart,
# JCP 52, 431 (1970); DOI:10.1063/1.1672702

gexps_1s = [2.310303149e01,4.235915534e00,1.185056519e00,
            4.070988982e-01,1.580884151e-01,6.510953954e-02]
gcoefs_1s = [9.163596280e-03,4.936149294e-02,1.685383049e-01,
             3.705627997e-01,4.164915298e-01,1.303340841e-01]

gexps_2s = [2.768496241e01,5.077140627e00,1.426786050e00,
            2.040335729e-01,9.260298399e-02,4.416183978e-02]
gcoefs_2s = [-4.151277819e-03,-2.067024148e-02,-5.150303337e-02,
             3.346271174e-01,5.621061301e-01,1.712994697e-01]

gexps_2p = [5.868285913e00,1.530329631e00,5.475665231e-01,
            2.288932733e-01,1.046655969e-01,4.948220127e-02]
gcoefs_2p = [7.924233646e-03,5.144104825e-02,1.898400060e-01,
             4.049863191e-01,4.012362861e-01,1.051855189e-01]

gexps_3s = [3.273031938e00,9.200611311e-01,3.593349765e-01,
            8.636686991e-02,4.797373812e-02,2.724741144e-02]
gcoefs_3s = [-6.775596947e-03,-5.639325779e-02,-1.587856086e-01,
             5.534527651e-01,5.015351020e-01,7.223633674e-02]

gexps_3p = [5.077973607e00,1.340786940e00,2.248434849e-01,
            1.131741848e-01,6.076408893e-02,3.315424265e-02]
gcoefs_3p = [-3.329929840e-03,-1.419488340e-02,1.639395770e-01,
             4.485358256e-01,3.908813050e-01,7.411456232e-02]
gexps_3d = [2.488296923,7.981487853e-1,3.311327490e-1,
            1.559114463e-1,7.877734732e-2,4.058484363e-2]
gcoefs_3d = [7.283828112e-3,5.386799363e-2,2.072139149e-1,
             4.266269092e-1,3.843100204e-1,8.902827546e-2]

gexps_4s = [3.232838646,3.605788802e-1,1.717902487e-1,
            5.277666487e-2,3.163400284e-2,1.874093091e-2]
gcoefs_4s = [1.374817488e-3,-8.666390043e-2,-3.130627309e-1,
             7.812787397e-1,4.389247988-1,2.487178756e-2]
gexps_4p = [2.389722618, 7.960947826e-1,3.415541380e-1,
            8.847434525e-2,4.958248334e-2,2.816929784e-2]
gcoefs_4p = [-1.665913575e-3,-1.657464971e-2,-5.958513378e-2,
             4.053115554e-1,5.433958189e-1,1.20970491e-1]

# Here are the STO-6G values from Hehre, Stewart, Pople JCP 51, 2657 (1969); DOI:10.1063/1.1672392
# and Hehre, Ditchfield, Stewart, Pople JCP 52, 2769 (1970); DOI:10.1063/1.1673374
# which are a little different, in that they use the same exponent for
# 2s,2p, and 3s,3p, which makes the fit a bit different.
gexps_old_2 = [1.03087e1,2.04036,6.34142e-1,
               2.43977e-1,1.05960e-1,4.85690e-2]
gcoefs_old_2s = [-1.32528e-2,-4.69917e-2,-3.37854e-2,
                 2.50242e-1,2.95117e-1,2.40706e-1]
gcoefs_old_2p = [3.75970e-3,3.76794e-2,1.73897e-1,
                 4.18036e-1,4.25860e-1,1.017008e-1]
gexps_old_3 = [3.0817,8.24896e-1,3.09345e-1,
               1.38468e-1,6.85210e-2,3.53133e-2]
gcoefs_old_3s = [-7.94313e-3,-7.10026e-2,-1.78503e-1,
                 1.51064e-1,7.35491e-1,2.76059e-1]
gcoefs_old_3p = [-7.13936e-3,-1.82928e-2,7.62162e-2,
                 4.14510e-1,4.88962e-1,1.05882e-1]

gexps = { # indexed by N,s_or_p:
    (1,0) : gexps_1s,
    (2,0) : gexps_2s,
    (2,1) : gexps_2p,
    (3,0) : gexps_3s,
    (3,1) : gexps_3p
}

gcoefs = {  # indexed by N,s_or_p:
    (1,0) : gcoefs_1s,
    (2,0) : gcoefs_2s,
    (2,1) : gcoefs_2p,
    (3,0) : gcoefs_3s,
    (3,1) : gcoefs_3p
}

gexps_old = { # indexed by N,s_or_p:
    (1,0) : gexps_1s,
    (2,0) : gexps_old_2,
    (2,1) : gexps_old_2,
    (3,0) : gexps_old_3,
    (3,1) : gexps_old_3
}

gcoefs_old = {  # indexed by N,s_or_p:
    (1,0) : gcoefs_1s,
    (2,0) : gcoefs_old_2s,
    (2,1) : gcoefs_old_2p,
    (3,0) : gcoefs_3s,
    (3,1) : gcoefs_3p
}

del(lib)
