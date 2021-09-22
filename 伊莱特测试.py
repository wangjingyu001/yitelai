import requests
import csv
import time
headers = {
        'Host': 'ylt.ikbvip.com',
        'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJkYXRlIjoiV2VkIFNlcCAyMiAwOTozOTozMiBDU1QgMjAyMSIsInBob25lIjoiMTU1MzY4MjYwNTMiLCJ0eXBlIjoiV1giLCJ1c2VySWQiOiI2NzgwIn0.z5RULJ0QUgAGJBbsLmi6YMSm1Akd_KT48EphpLtVAGPkCGowasEKqrH6wygERD1zrB9co4Afs3cTF9sUF7X6_w',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'content-type': 'application/json',
        'referer': 'https://servicewechat.com/wxf077d1a84a951991/16/page-frame.html',
    }
def get_data():


    data = {"filterType":"1",
            "stationLng":"116.44355",
            "stationLat":"39.9219",
            "pageNum":1,
            "pageSize":5,
            "isParkFee":"",
            "serviceItem":"",
            "isOpen":"",
            "chargeSettleType":"",
            "stationName":"",
            "userId":6780}
    try:
        response = requests.post('https://ylt.ikbvip.com/stationapi/station/queryNearbyStation',verify =False, headers=headers, json=data)
        # print(response.text)
        rpjs = response.json()
    except:
        return
        pass
    data_list = rpjs.get('data','').get('list','')
    for item in data_list:
        stationName = item.get('stationName','')
        address = item.get('address','')
        parkFee = item.get('parkFee','')
        stationLocationTypeMsg = item.get('stationLocationTypeMsg','')
        with open(f'data{str(int(time.time()))}.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            # writer.writerow('采集点&位置&具体位置&快充剩余&快充总量&慢充剩余&慢充总量&原价&现价&折扣&充电站厂家'.split('&'))

            writer.writerow([stationName,address,parkFee,stationLocationTypeMsg])


get_data()