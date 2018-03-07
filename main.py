from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/<message>")
def hello(message):
    res = custom_response(hit_simsimi(message) )
    return jsonify(res) 


def custom_response( response ):
    dic = {
            "status": 200,
            "message": "success",
            "data": {
                "message": response['simsimi_talk_set']['answers'][0]['sentence']
            }
        }
    return dic

def hit_simsimi( msg ):
    url = "http://www.simsimi.com/otn/talk"
    querystring = {"talkCnt":"2","reqText": msg}
    headers = {
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "id,en;q=0.9",
            'Cache-Control': "no-cache",
            'Connection': "keep-alive",
            'Cookie': "dotcom_session_key=s%3ADZ2djqlVs-DGk8ytAf_E9x5dkENoHdkd.TN6hQ6oAEUCn4QPgwdMXqIKsdyJLSgK9gysai%2FDcxvs; _ga=GA1.2.1691868767.1519388238; _gid=GA1.2.1941626242.1519388238; io=pA8546xih6_1zXoyAAzX",
            'Host': "www.simsimi.com",
            'If-None-Match': "W/\"1f5-ydvijGdp6ZVzqp4n2nbIlw\"",
            'Upgrade-Insecure-Requests': "1",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 YaBrowser/18.1.1.841 Yowser/2.5 Safari/537.36",
            'Postman-Token': "09c3e89b-a369-4b5b-960c-48b968a20c8b"
            }

    response = requests.request("GET", url, headers=headers, params=querystring)
    parse =  json.loads(response.text)
    parse2 = json.loads(parse)
    return parse2 


