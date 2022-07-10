import requests
import pandas as pd
url = "https://api.ambeedata.com/latest/by-lat-lng"
querystring = {"lat":"49.45","lng":"11.0767"}
headers = {
	'x-api-key': "87b81af771c4624f163c312186327b1102dd70bf75acde43e0668d007d7a028e",
	'Content-type': "application/json"
	}
response = requests.request("GET", url, headers=headers, params=querystring)

#df = pd.DataFrame(response)
str_df = response.text
print(str_df)
print(response.text)