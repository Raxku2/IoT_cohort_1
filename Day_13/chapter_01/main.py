# print('Hello Universe')

# from requests import get

# print(get('google.com'))


# import time
# a = 1
# while True:
   # a += 1
   # time.sleep(2)
   #  print(a)


# from flask import Flask
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def root():
#     return """<div style="height:20px; background-color:red;"> ok</div>"""
#
from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'ok'

89


"abcd"

"""

its an  multtiline strin
used as ancomment
"""










