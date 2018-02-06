#-*- coding:utf-8 -*-

from flask import Flask, request;
from flaskext.mysql import MySQL;
import json;
import properties;

app = Flask(__name__)
mysql = MySQL();

app.config['MYSQL_DATABASE_USER'] = properties.getDatabaseUser();
app.config['MYSQL_DATABASE_PASSWORD'] = properties.getDatabasePassword();
app.config['MYSQL_DATABASE_DB'] = properties.getDatabaseDB();
app.config['MYSQL_DATABASE_HOST'] = properties.getDatabaseHost();

mysql.init_app(app);


@app.route('/keyboard')
def keyboard():
    result = {
        "type" : "text"
    }
    return json.dumps(result);

@app.route('/message', methods=['POST'])
def message():

    message = request.get_json();
    content = message['content']

    print(content)

    if content == u"시작하기":
        result = {
            "message": {
                "text": "아직 개발중이라 대답을 잘 못해도 이해해줘^^;"
            }
        }
    elif content == u"도움말":
        result = {
            "message": {
                "text": "이제 곧 정식 버전이 출시될거야. 조금만 기다려~~~"
            }
        }
    elif u"안녕" in content:
        result = {
            "message": {
                "text": "안녕~~ 반가워 ㅎㅎ"
            }
        }
    else:
        result = {
            "message": {
                "text": "나랑 놀자 ㅋㅋㅋ"
            }
        }
    return json.dumps(result)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=properties.getPort())
