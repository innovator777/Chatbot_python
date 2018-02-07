#-*- coding: utf-8 -*-

from flask import Flask, request;
from flaskext.mysql import MySQL;
import json;
import properties;
import answer;
import check;
import database;

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

@app.route('/message', methods=["GET", "POST"])
def message():

    message = request.get_json();
    content = message['content']

    print(content)

    if content == u"사용방법":
        result = answer.getManual();
    elif content == u"소개":
        result = answer.getIntroduce();
    elif content == u"지원요건":
        result = answer.getApplyConditions();
    elif content == u"지원방법":
        result = answer.getApplyInformation();
    elif check.applyCondition(content):
        cursor = mysql.get_db().cursor();
        cursor.execute(database.getAddTarget(), content);
        # mysql.connect().commit();
        mysql.get_db().commit();
        result = answer.getApplySuccess();
    elif check.managerCommand(content):
        cursor = mysql.get_db().cursor();
    	cursor.execute(database.getAllTarget());

        # rows = cursor.fetchall();
        # array = []
        # for first, second in rows:
        #     array.append("%s. %s" % (first ,second));
        #
        # message = ""
        # for data in array:
        #     message = message + data + '\n'

        rows = cursor.fetchall();
        message = ""
        for first, second in rows:
            message = message + "%s. %s" % (first ,second) + '\n';

        result = {
            "message": {
                "text": message
            }
        }

    else:
        result = answer.getDefault();

    return json.dumps(result)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=properties.getPort())
