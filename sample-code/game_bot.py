#!/usr/bin/python
#coding=utf-8

import os
import time
import re
import random
from slackclient import SlackClient

# 先在環境變數設定 Slack bot token
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')

# 104 hackathon chatbot 的 user id
HACKATHON_BOT_USER_ID = "UANUQ2XCN"

# 積分賽-是非題-頻道
POINT_GAME_TF_CHANNEL_ID = "CAZ2MEA9G"    #point-game-1

# 積分賽-選擇題-頻道
POINT_GAME_MC_CHANNEL_ID = "CAYBKB60G"    #point-game-2

# 積分賽-填空題-頻道
POINT_GAME_BF_CHANNEL_ID = "CB041587R"    #point-game-3

# 決賽-混合題-頻道
FIANL_GAME_CHANNEL_ID = "CAYREHJ7N"     #final-game

# 從 RTM 讀取訊息的延遲時間，單位是秒
RTM_READ_DELAY = 0.1

# 初始化 slack client
slack_client = SlackClient(SLACK_BOT_TOKEN)


def parse_bot_events(slack_events):
    for event in slack_events:
        print(event)
        if event.get("type") == "message" and event.get("subtype") == "bot_message":    # 只回應 bot 的訊息
            message = event.get("text")
            return message, event.get("channel")
    return None, None

def send_private_message(user_id, channel_id, text):
    response = slack_client.api_call(
        "chat.postEphemeral",
        channel=channel_id,
        user=user_id,
        text=text
    )
    print("postEphemeral.ok=%s" % response.get(u"ok"))

def send_public_message(channel_id, text):
    response = slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=text
    )
    print("postMessage.ok=%s" % response.get(u"ok"))

def true_or_false_question(question_id, question_type, question_from, question_score, question):
    answer = "O"
    response = "Id: " + question_id + "\n"
    response += "Answer: " + answer
    return response

def multiple_choice_question(question_id, question_type, question_from, question_score, question):
    answer = "1"
    response = "Id: " + question_id + "\n"
    response += "Answer: " + answer
    return response

def blank_filling_question(question_id, question_type, question_from, question_score, answer_length, question):
    answer = u"三十年"
    response = "Id: " + question_id + "\n"
    response += "Answer: " + answer
    return response

def handle_command(command, channel):

    # 如果是題目，應該會包含 Question 字串
    if "Question:" not in command:
        return

    command_split = command.split("\n")
    for str in command_split:
        str = str.strip()
        if str.startswith("Id:"):
            question_id = str.split("Id:")[1].strip()
        elif str.startswith("Type:"):
            question_type = str.split("Type:")[1].strip()
        elif str.startswith("From:"):
            question_from = str.split("From:")[1].strip()
        elif str.startswith("Score:"):
            question_score = str.split("Score:")[1].strip()
        elif str.startswith("Length:"):
            answer_length = str.split("Length:")[1].strip()

    # 取得題目內容
    if "Question:" in command:
        question = command.split("Question:")[1].strip()

    # 這裡是回答
    response = None
    if question_type == u"是非題":
        response = true_or_false_question(question_id, question_type, question_from, question_score, question)
    elif question_type == u"選擇題":
        response = multiple_choice_question(question_id, question_type, question_from, question_score, question)
    elif question_type == u"填空題":
        response = blank_filling_question(question_id, question_type, question_from, question_score, answer_length, question)

    # 確認目前是哪個賽程
    if channel == FIANL_GAME_CHANNEL_ID:
        send_public_message(channel, response)    # 決賽直接回在頻道裡
    else:
        send_private_message(HACKATHON_BOT_USER_ID, channel, response)    # 積分賽回私訊

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("GameBot connected and running!")
        while True:
            command, channel = parse_bot_events(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed.")
