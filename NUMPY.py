import numpy as np
#a=np.array([[1,2,3,4],[6,7,8,9]])
#print(a)
#print(a[:,-1:0:-2])
#a=np.ones((5,5))
#a[1:4,1:4]=0
#a[2,2]=9
#print(a)
#d={"cap":[{}]}
#d["cap"]["capiyal"]="che"
#d["state"]="tn"
import requests
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"hourly": "temperature_2m"
}

a=requests.get(url = "https://api.open-meteo.com/v1/forecast", params=params)

print(a.json())





