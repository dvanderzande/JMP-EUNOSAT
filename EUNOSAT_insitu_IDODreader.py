"""
Created on 20170910
@author: Dimitry Van der Zande (dvanderzande@naturalsciences.be)
routine accepting IDOD exports as input which reformats them to EUNOSAT format

*input: IDOD export
*output: CVS EUNOSAT format
"""

#import
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import RegularGridInterpolator as rgi
import os
import matplotlib.pyplot as plt

#modules
def read_IDODdata(fpath):
    #function to read data downloaded from https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20170819
    IDOD = []
    with open(fpath) as file:
        for line in file:
            line = line.strip()
            line_spl = line.split('\t')
            IDOD.append(line_spl)
    return IDOD

fpath = 'D:/Dimitry/000_Python/PyCharm/EUNOSAT/data/insitu/Request_Dimy_20170825.txt'
IDOD = read_IDODdata(fpath)

#location name	latitude (decimal)	longitude (decimal)	used for MSFD-assessment (Y/N)	year	date	time	depth of sample, m below the surface	salinity	temperature	AMON BSI NTOT NTRA NTRI NITRZ PHOS SIO2 SLCA chlorophyll	spm  Turb Method
data_EUNOSAT_AMON = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,AMON,unit,Method'
data_EUNOSAT_AMON.append(header)

data_EUNOSAT_BSI = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,BSI,unit,Method'
data_EUNOSAT_BSI.append(header)

data_EUNOSAT_CPHL = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,CPHL,unit,Method'
data_EUNOSAT_CPHL.append(header)

data_EUNOSAT_NTOT = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,NTOT,unit,Method'
data_EUNOSAT_NTOT.append(header)

data_EUNOSAT_NTRA = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,NTRA,unit,Method'
data_EUNOSAT_NTRA.append(header)

data_EUNOSAT_NTRI = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,NTRI,unit,Method'
data_EUNOSAT_NTRI.append(header)

data_EUNOSAT_NTRZ = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,NTRZ,unit,Method'
data_EUNOSAT_NTRZ.append(header)

data_EUNOSAT_PHOS = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,PHOS,unit,Method'
data_EUNOSAT_PHOS.append(header)

data_EUNOSAT_SIO2 = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,SIO2,unit,Method'
data_EUNOSAT_SIO2.append(header)

data_EUNOSAT_SLCA = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,SLCA,unit,Method'
data_EUNOSAT_SLCA.append(header)

data_EUNOSAT_SUSP = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,SUSP,unit,Method'
data_EUNOSAT_SUSP.append(header)

data_EUNOSAT_TURB = []
header = 'location name,latitude,longitude,used for MSFD-assessment (Y/N),date,depth of sample,TURB,unit,Method'
data_EUNOSAT_TURB.append(header)
MSFDproject =['MONIT_SEAWATER_MUMM','MONIT_SEAWATER_MUMM;WFD_ODNature','WFD_ODNature;MONIT_SEAWATER_MUMM','WFD_ODNature','WFD_003_LPAE']
for i in range(1,len(IDOD)):
    loc = IDOD[i][6]
    lat = IDOD[i][8]
    lon = IDOD[i][9]
    project = IDOD[i][29]
    try:
        b=MSFDproject.index(project)
    except ValueError:
        MSFD = 'N'
    else:
        MSFD = 'Y'

    # if project == ['MONIT_SEAWATER_MUMM','MONIT_SEAWATER_MUMM;WFD_ODNature','WFD_ODNature;MONIT_SEAWATER_MUMM','WFD_ODNature','WFD_003_LPAE']:
    #     MSFD = 'Y'
    # else:
    #     MSFD = 'N'
    date =  IDOD[i][3]
    depth = IDOD[i][15]
    variable = IDOD[i][20]
    pval = IDOD[i][23]
    unit = IDOD[i][24]
    method = IDOD[i][27]
    QC = IDOD[i][26]

    if QC == 'Acceptable':

        println = loc+',' + lat +','+ lon +','+ MSFD +','+ date +','+ depth +','+ pval +','+ unit +','+ method

        if variable == 'AMON':
            data_EUNOSAT_AMON.append(println)
        if variable == 'BSI':
            data_EUNOSAT_BSI.append(println)
        if variable == 'CPHL':
            data_EUNOSAT_CPHL.append(println)
        if variable == 'NTOT':
            data_EUNOSAT_NTOT.append(println)
        if variable == 'NTRA':
            data_EUNOSAT_NTRA.append(println)
        if variable == 'NTRI':
            data_EUNOSAT_NTRI.append(println)
        if variable == 'NTRZ':
            data_EUNOSAT_NTRZ.append(println)
        if variable == 'PHOS':
            data_EUNOSAT_PHOS.append(println)
        if variable == 'SIO2':
            data_EUNOSAT_SIO2.append(println)
        if variable == 'SLCA':
            data_EUNOSAT_SLCA.append(println)
        if variable == 'SUSP':
            data_EUNOSAT_SUSP.append(println)
        if variable == 'TURB':
            data_EUNOSAT_TURB.append(println)


fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/AMON_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_AMON:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/BSI_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_BSI:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/CPHL_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_CPHL:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/NTOT_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_NTOT:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/NTRA_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_NTRA:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/AMON_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_AMON:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/NTRI_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_NTRI:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/NTRZ_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_NTRZ:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/PHOS_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_PHOS:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/SIO2_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_SIO2:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/SLCA_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_SLCA:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/SUSP_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_SUSP:
        file_handler.write("{}\n".format(item))

fpath = 'k:/JMP EUNOSAT/in situ/BE/IDOD/TURB_BE.txt'
with open(fpath, 'w') as file_handler:
    for item in data_EUNOSAT_TURB:
        file_handler.write("{}\n".format(item))






