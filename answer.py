#-*- coding:utf-8 -*-

def getManual():
    result = {
        "message": {
            "text": "1. 소개\n"
					+ "2. 지원요건\n"
					+ "3. 지원방법\n"
					+ "\n\n"
					+ "ex)소개"
        }
    }
    return result;

def getIntroduce():
    result = {
        "message": {
            "text": "안녕하세요\n" +
					"먼저 학우분의 관심에 감사인사드립니다.\n" +
					"저희는 백석대학교 정보통신학부 소프트웨어학과 LAB 입니다.\n" +
					"위치는 본부동 11층 1114호에 있으며, ... 중략...\n"
        }
    }
    return result;

def getApplyConditions():
    result = {
        "message": {
            "text": "저희 LAB은 현재 2~3학년 학우분들을 대상으로 지원 받고 있으며,\n" +
					"남학우분의 경우에는 군복무를 마치신 학우분을 대상으로 지원 받고 있습니다.\n" +
					"아직 군복무를 마치지 못한 남학우분은 군복무를 마치신 후에 다시 지원부탁드립니다. " +
					"...중략...\n"
        }
    }
    return result;

def getApplyInformation():
    result = {
        "message": {
            "text": "'지원요건' 내용에 부합하신 분이라는 가정하에 지원접수 절차를 진행하도록 하겠습니다.\n" +
					"안내 메세지를 잘 읽으시고 응답해주시면 됩니다.\n\n" +
					"이름/성별/학번/학과/핸드폰번호/면접가능한 요일 및 시간대\n\n"
                    + "ex)김영희/여자/20160001/01012345678/월~수 오후 3시 이후"
        }
    }
    return result;

def getDefault():
    result = {
        "message": {
            "text": "다시 입력해주세요."
        }
    }
    return result;

def getApplySuccess():
    result = {
        "message": {
            "text": "지원접수가 되었습니다.\n"
                    + "추후 연락드리겠습니다.\n"
                    + "감사합니다."
        }
    }
    return result;

def getApplyFail():
    result = {
        "message": {
            "text": "지원접수를 실패하였습니다.\n"
						+ "다시 입력해주세요"
        }
    }
    return result;
