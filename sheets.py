import pygsheets

client = pygsheets.authorize(service_account_file='secret.json')
sheet = client.open_by_key('1kF05N3kjYWG_oTJTeteCX5PDcB2RqOCC1FPBxst6nUo')
wks = sheet.worksheet_by_title('Data')
for i in range(10):
  wks.insert_rows(i+1, values=["fsdfsd", "dfs", "fdsdfs"])