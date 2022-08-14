# Rad_RadKern_fdbk_cmip56

[![DOI](https://zenodo.org/badge/424397920.svg)](https://zenodo.org/badge/latestdoi/424397920)

## Description
This repo is used to save 
- feedbacks derived from (1) traditional Hansen or Gregory method (Gregory et al., 2004) -- RadFeedback, (2) radiative kernel method (i.e., Soden et al., 2004) -- RadKernFeedback. 
- effective radiative forcing (ERF).
These data ared used in Qin et al. (2020).

### Experiments used 
These feedbacks derived from a series of CMIP experiments:
- piControl and abrupt-4xCO2
- amip and amip-p4K
- amip and amip-future4K
- aquaControl and aqua-p4K

ERFs derived from CMIP experiments:
- piControl and abrupt-4xCO2
- amip and amip-4xCO2
- sstClim and sstClim4xCO2 [CMIP5] or piClim-control and piClim-4xCO2 [CMIP6]

### Files 
- Radiaitve feedbacks are saved in: RadFeedabck_cmip56.json

- Radiative kernel feedbacks are saved in: RadKernFeedback_cmip56.json

- ERFs are saved in: RadERF_cmip56.json

### Demo
read.py can be used to read these data. Overall, the data structure is: [experiment][phase][model and ripf][feedback_var]

For ERFs, the data structure is: [experiment][phase][model and ripf]

### Acronyms
1. experiments

| Acronyms      | Description |
| ----------- | ----------- |
|   1-150yr_abrupt    | use full 150-year piControl and abrupt-4xCO2       |
| 1-20yr_abrupt   | use first 20-year piControl and abrupt-4xCo2       |
| 21-150yr_abrupt | use last 130-year piControl and abrupt-4xCO2 |
| amip4K | use amip and amip-p4K | 
| amipfuture | use amip and amip-future4K |
| aqua4K | use aquaControl and aqua-p4K |
| amip4xCO2 | use amip and amip-4xCO2 | 
| sstClim | use sstClim and sstClim4xCO2 for CMIP5, piClim-control and piClim-4xCO2 for CMIP6 | 

2. phases

| Acronyms      | Description |
| ----------- | ----------- |
| 'CMIP5' | only CMIP5 models |
| 'CMIP6' | only CMIP6 models |
| 'CMIP56' | CMIP5 and CMIP6 models |

3. feedbacks from RadFeedback [W/m2/K]
  
| Acronyms      | Description |
| ----------- | ----------- |
| FTOA | net TOA radiation |
| netCRE | net cloud radiation effect (CRE) |
|SWCRE | SW CRE |
| LWCRE | LW CRE |
| FSNT | TOA SW radiation |
| FLNT | TOA LW radiation |
| SWCLR | clear-sky SW TOA radiation |
| LWCLR | clear-sky LW TOA radiation |
| FTOACLR | clear-sky total TOA radiation |


3. feedbacks from RadKernFeedback [W/m2/K]
  
| Acronyms      | Description |
| ----------- | ----------- |
| PL | Planck |
| LR | Lapse rate |
| WV | water vapor |
| PL_fxRH | constant-RH Planck |
| LR_fxRH | constant-RH lapse rate |
| RH | relative humidity |
| ALB | albedo |
| SWCLD | shortwave cloud |
| LWCLD | longwave cloud |
| TOTCLD | total cloud |
| ERR | residual |

