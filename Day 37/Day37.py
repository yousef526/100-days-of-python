"""
Http requests
Get: when you want to get data from external resoures
Post: when you want to send data to external resoures
Put" When you want to updata piece of information somewhere
Delete: When you want to delete an info"""


"https://pixe.la/@yousefalaa"

import requests
import datetime as dt 

################################ creating my email
pixela_endPoint = "https://pixe.la/v1/users"
pixela_Params = {
    "token":"abdwQTFA%$mold5454#$DBmsl",
    'username':"yousefalaa",
    "agreeTermsOfService":'yes',
    'notMinor':'yes',
}

""" response = requests.post(url=pixela_endPoint,json=pixela_Params)
print(response.text) """
#################################################



## creating the dashboard
graph_endpoint = f"{pixela_endPoint}/{pixela_Params['username']}/graphs"

graph_params = {
    "id": "graph1",
    "name":"Gaming",
    "unit":"hours",
    "type":'float',
    'color':'ajisai',
}

HEADER = {
    "X-USER-TOKEN":"abdwQTFA%$mold5454#$DBmsl"
}

""" response = requests.post(url=graph_endpoint,json=graph_params,headers=HEADER)
print(response.text) """


#####################################################



## adding a colored pixel

pixel = "https://pixe.la/v1/users/yousefalaa/graphs/graph1"

pixel_header = {
    "X-USER-TOKEN": pixela_Params["token"],
}

now = dt.datetime.now()
today_date = str(now.now().date()).replace('-','')
#print(today_date)

pixel_body = {
    "date":today_date,#"20230827",#20230801
    "quantity":"9.5",
}

""" response = requests.post(url=pixel,json=pixel_body,headers=HEADER)
print(response.text) """

###########################################



## update a pixel

api_Update = "https://pixe.la/v1/users/yousefalaa/graphs/graph1/20230801"

api_body = {
    "quantity":"16",
}

""" response = requests.put(url=api_Update,json=api_body,headers=HEADER)
print(response.text) """
############################


## delete pixel

api_Delete = "https://pixe.la/v1/users/yousefalaa/graphs/graph1/20230827"

""" response = requests.delete(url=api_Delete,headers=HEADER)
print(response.text) """