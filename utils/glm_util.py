import time
import openai
from zhipuai import ZhipuAI
from applications.glm import gpt
from tenacity import retry, stop_after_attempt, wait_random_exponential, wait_fixed
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask import Flask, request, session, redirect
from extensions.init_login import *
from settings import Config


def generate_word_analysis_report(brand1, related_word):
    api_key = Config.api_key
    if api_key:
        words = ""
        for word in related_word:
            words = words + word
        print("搜索词"+brand1+"相关词"+words)
        client = ZhipuAI(api_key=api_key)
        prompt = f" 请注意不要有任何和时间相关的警告说明，请用中文回答并简单的介绍\"{brand1}\"，要求简短精炼,一定要在50字以内,请注意这里的\"{brand1}\"的相关词是\"{words}\"，你可以做参考，不要误解了这里\"{brand1}\"的意思"
        response = client.chat.completions.create(
            model="GLM-4-Flash",  # 填写需要调用的模型编码
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        session['content1'] = response.choices[0].message.content
        return response.choices[0].message.content
    else:
        return "GPT的key没有给定，这是一条默认的文本"

def generate_word_analysis_report_seedword(brand1, related_word):
    api_key = Config.api_key
    if api_key:
        words = ""
        for word in related_word:
            words = words + word+","
        print("搜索词"+brand1+"相关词"+words)
        client = ZhipuAI(api_key=api_key)
        prompt = f" 请注意不要有任何和时间相关的警告说明，请用中文回答并简单的介绍\"{brand1}\"，要求简短精炼,一定要在50字以内,请注意这里的\"{brand1}\"的相关词是\"{words}\"，你可以做参考，不要误解了这里\"{brand1}\"的意思"
        response = client.chat.completions.create(
            model="GLM-4-Flash",  # 填写需要调用的模型编码
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        session['content1'] = response.choices[0].message.content
        return response.choices[0].message.content
    else:
        return "GPT的key没有给定，这是一条默认的文本"
