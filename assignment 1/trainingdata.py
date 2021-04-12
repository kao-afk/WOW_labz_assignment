import pandas as pd
import numpy as np

dic={4:.01,5:.05,6:.3,7:.3,8:.3,9:.03,10:.01} ## percentage

sleep_hours=[]
active_hours=[]
for k in dic.keys():
  no=dic[k]*200
  no=int(no)
  for e in range(no):
    sleep_hours.append(k)
    if k in [4,5,6,7]:
      active_hours.append(24-k+np.random.randint(-2,0))
    else:
      active_hours.append(24-k+np.random.randint(0,2))  

d=pd.DataFrame({"Sleep hours":sleep_hours,"active hours":active_hours})
dic={ 2:.06, 3:.2, 4:.44, 5:.3 } ## percentage
for k in dic.keys():
  no=dic[k]*50
  no=int(no)
  if k==2:
    s_low=3
    s_high=4
    a_low=5
    a_high=6

  if k==3:
    s_low=2
    s_high=4
    a_low=5
    a_high=7

  if k==4:
    s_low=1
    s_high=3
    a_low=6
    a_high=10
  
  if k==5:
    s_low=1
    s_high=2
    a_low=7
    a_high=10           
  
  for e in range(no):
    second_sleep_hrs=np.random.randint(s_low,s_high)
    active_before_second=np.random.randint(a_low,a_high)
    sleep_hours.append([k,second_sleep_hrs])
    active_hours.append([active_before_second,24-k-second_sleep_hrs-active_before_second])
a=np.arange(0,250,1)
np.random.shuffle(a)
active=[]
sleep=[]
for x in a:
  if type(sleep_hours[x]) is list:
    sleep.append(sleep_hours[x][0])
    active.append(active_hours[x][0])
  else:
    sleep.append(sleep_hours[x])
    active.append(active_hours[x])

d=pd.DataFrame({"Sleep hours":sleep,"Active hours":active})
d.to_csv("trainingdata.txt",sep="\t",index=False)