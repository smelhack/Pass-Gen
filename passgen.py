# -*- coding:utf -8 -*-
#!/usr/bin/python3

import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style


banner = """
 ____________________________________________________
|                                                    |
| [--] Name: PassGen                                 |
|                                                    |
| [--] Generation Password                           |
|                                                    |
| [--] Created by: https://vk.com/death_me3          |
|                                                    |
| [--] Version: 1.0.0                                |
|____________________________________________________|
"""

print(banner)


chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int(input('Количество паролей?'+ "\n"))

length = int(input('Длина пароля?'+ "\n"))

for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)
os.system('pause')
