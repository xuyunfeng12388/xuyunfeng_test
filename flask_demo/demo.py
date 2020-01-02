import csv
import re
import sys
import os
import uuid



pwd = os.path.dirname(os.path.realpath(__file__))
print(pwd)
sys.path.append(pwd+"/" + "watch_apply/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watch_apply.settings.dev")  #配置系统变量
import django
django.setup()

# # 4174
# from puzzles.models import  Puzzle
#
# app_list = os.listdir("./image/动物_slices")
# print(app_list)
# for filename in app_list:
#     print(filename)
#     with open("image/动物_slices/" + filename, 'rb') as f:
#         data = f.read()
#
#     """将二进制文件数据转换为InMemoryUploadedFile文件对象"""
#     from django.core.files.uploadedfile import InMemoryUploadedFile
#     from io import BytesIO
#     f1 = BytesIO()
#     f1.write(data)
#
#     # InMemoryUploadedFile 需要的参数：
#     # file, field_name, name, content_type, size, charset, content_type_extra = None
#     watch_image = InMemoryUploadedFile(f1, None, str(uuid.uuid1()) + '.png', None, len(data), None, None)
#     Puzzle.objects.create(puzzles_url= watch_image, category_id=4)

# with open("猜字大师.txt", "r")as f:
#     content = f.read()
#     print(content)
#     replace_content = re.sub(r"猜一字，答案是", "猜一个字答案是", content)
    # print(replace_content)
# with open("猜字大师.txt", 'w')as f:
#     f.write(replace_content)

# with open("猜字大师.txt", "r", encoding="gbk")as f:
#     while True:
#         content = f.readline()
#         if not content:
#             break
#         print(content)
#         content_list = re.split(r"[\.\: \n]", content)
#         print(content_list, "content_list")
#         print(content_list[0])
#         print(content_list[1][3:-8])
#         print(content_list[2])
#         WordPuzzle.objects.create(
#             answer= content_list[2],
#             the_answer=content_list[1][3:-8],
#             sequence= int(content_list[0])
#        )

import random
from applys.models import GuessWord
guessword = GuessWord.objects.all()
print(guessword)
for guess in guessword:
    numbers = ["1", "2", "3", "4"]
    chosen = random.sample(numbers, random.randint(0, 1))
    number = ''.join(chosen)
    print(number)
    # guess.prompt_word = number
    # guess.save()




