
import json

f = open('RadFeedback_CMIP56.json','r')
data = json.load(f)

print(data.keys())
print(data['amip4K'].keys())
print(data['amip4K']['CMIP56'].keys())
print(data['amip4K']['CMIP56']['bcc-csm1-1_r1i1p1'].keys())
print(data['amip4K']['CMIP56']['bcc-csm1-1_r1i1p1']['FTOA'])




f = open('RadKernFeedback_CMIP56.json','r')
data = json.load(f)

print(data.keys())
print(data['amip4K'].keys())
print(data['amip4K']['CMIP56'].keys())
print(data['amip4K']['CMIP56']['bcc-csm1-1_r1i1p1'].keys())
print(data['amip4K']['CMIP56']['bcc-csm1-1_r1i1p1']['PL'])


