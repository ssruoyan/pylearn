import requests
import json
import xlwt

data = requests.get(
  'https://hq.itradeup.com/stock_info/candle_stick/5min/RBLX?deviceId=9d7ab87c-30a7-4e0f-8470-9305ffe68654&platform=desktop-web&vendor=web&region=USA&location=HKG&lang=en_US&beginTime=-1&endTime=-1&right=br&limit=10000',
  headers={
    'Connection': 'keep-alive',
    'Origin': 'https://web.tradeup.marsco.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Authorization': 'Bearer rok07aJCZo4lmv0FBkRPKW4Sh6yXmq',
    'Referer': 'https://web.tradeup.marsco.com/'
  }).json()
data2 = requests.get(
  'https://hq.itradeup.com/stock_info/candle_stick/60min/RBLX?deviceId=9d7ab87c-30a7-4e0f-8470-9305ffe68654&platform=desktop-web&vendor=web&region=USA&location=HKG&lang=en_US&beginTime=-1&endTime=-1&right=br&limit=1000',
  headers={
    'Connection': 'keep-alive',
    'Origin': 'https://web.tradeup.marsco.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Authorization': 'Bearer rok07aJCZo4lmv0FBkRPKW4Sh6yXmq',
    'Referer': 'https://web.tradeup.marsco.com/'
  }).json()

wb = xlwt.Workbook(encoding = 'utf-8')
sheet1 = wb.add_sheet('RBLX 5m quotes')
sheet2 = wb.add_sheet('RBLX 60m quotes')

items1 = data['items']
items2 = data2['items']

print(items2)

def write_data(sheet, items):
  sheet.write(0, 0, '收盘价')
  sheet.write(0, 1, '开盘价')
  sheet.write(0, 2, '成交量')
  for index in range(len(items)):
    sheet.write(index + 1, 0, items[index]['close'])
    sheet.write(index + 1, 1, items[index]['open'])
    sheet.write(index + 1, 2, items[index]['volume'])

write_data(sheet1, items1)
write_data(sheet2, items2)

wb.save('candles.xls')
