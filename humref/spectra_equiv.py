''''spectra_equiv.py takes in Spectra Sensor measurements and calculates equivalent 
relative humidity and dew point.'''

import CoolProp.CoolProp as cp
import CoolProp.HumidAirProp as hap
import pandas as pd

# Conversion constants
FT2M = 3.208        # Distance ft to m
K2R = 1.8           # Temperature K to degR
KPA2PSI = 0.145038  # Pressure kPa to psi
KGM2LBFT = 0.062428 # Density kg/m^3 to lbm/ft^3

# Standard constants
MAIR = cp.PropsSI('M','T',300,'P',101325,'air')*1e3  # Molar mass of dry air (g/mol)
MH2O = cp.PropsSI('M','T',300,'P',10.1,'water')*1e3  # Molar mass of water (g/mol)


# Vapor pressure calculation (checked and PASSED)
#  inputs: mmr     mass mixing ratio
#          p_psi   pressure in area of sample (psi)
#  output: p_w     vapor pressure (psi)
def vapor_pressure(mmr, p_psi):
    p_w = p_psi * mmr / (MH2O / MAIR + mmr)

    return p_w


# Dew Point calculation (checked and PASSED)
#  inputs: mmr     mass mixing ratio
#          p_psi   pressure in area of sample (psi)
#  output: t_d     dew point temperature (F)
def dew_point(mmr, p_psi):
    # Vapor pressure
    p_w_psi = vapor_pressure(mmr, p_psi)

    # Convert to SI units
    p_w = p_w_psi / (KPA2PSI/1000)
    p = p_psi / (KPA2PSI/1000)

    # # ASHRAE method
    # t_d = 90.12 + 26.412 * np.log(p_w) + 0.8927 * np.log(p_w)**2

    # CoolProp method
    t_d = hap.HAPropsSI('D','W',mmr,'P',p,'T',300)

    return (t_d-273.15)*9/5 + 32  # converted to degreesF


# Relative humidity calculation (checked and PASSED)
#  inputs: t_f     temperature in area of sample (degF)
#          mmr     mass mixing ratio
#          p_psi   pressure in area of sample (psi)
#  output: rh      relative humidity (0-100)
def relative_humidity(t_f, mmr, p_psi):
    # Convert to SI units
    t = (t_f-32)*5/9 + 273.15   # Kelvin
    p = p_psi / (KPA2PSI/1000)  # Pascals
    
    # Calculate dew point (K)	
    t_d = (dew_point(mmr,p_psi)-32)*5/9 + 273.15

    # CoolProp
    rh = hap.HAPropsSI('R','T',t,'D',t_d,'P',p)

    return rh*100


# Calculate ratio of specific heats
#  inputs:  t     temperature (degF)
#           p     pressure (psi)
#           mmr   mass mixing ratio (kgDA/kgWV)
#  output:  gam   mixture ratio of specific heats
def gamma(t,p,mmr):
    t_K = (t-32)*5/9 + 273.15     # Kelvin
    p_Pa = p / (KPA2PSI/1000)     # Pascals

    p_w = p_Pa * mmr / (mh2o/mair + mmr)  # vapor pressure (Pa)
    p_a = p_Pa - p_w   # partial pressure of air (Pa)

    cp = 'CPMASS'
    cv = 'CVMASS'
    gam_air = cpp.PropsSI(cp,'T',t_K,'P',p_a,'air')/cpp.PropsSI(cv,'T',t_K,'P',p_a,'air')
    gam_h2o = cpp.PropsSI(cp,'T',t_K,'P',p_w,'water')/cpp.PropsSI(cv,'T',t_K,'P',p_w,'water')

    w_h2o = mmr/(1+mmr)   # specific humidity (mass fraction water vapor)
    w_air = 1 - w_h2o     # mass fraction of dry air
    
    gam_mix = gam_air*w_air + gam_h2o*w_h2o   # gamma of mixture

    return gam_mix


# Calculate humid air density
#  inputs:  t     temperature (degF)
#           p     pressure (psi)
#           mmr   mass mixing ratio (kgDA/kgWV)
#  output:  rho   mixture density (lbm/ft3)
def density(t,p,mmr):
    t_K = (t-32)*5/9 + 273.15     # Kelvin
    p_Pa = p / (KPA2PSI/1000)     # Pascals

    p_w = p_Pa * mmr / (mh2o/mair + mmr)  # vapor pressure (Pa)
    p_a = p_Pa - p_w   # partial pressure of air (Pa)

    rho_air = cpp.PropsSI('D','T',t_K,'P',p_a,'air')    # density kg/m3
    rho_h2o = cpp.PropsSI('D','T',t_K,'P',p_w,'water')  # density kg/m3
    rho_mix = (rho_air + rho_h2o) * kgm2lbft           # density lbm/ft3

    return rho_mix


