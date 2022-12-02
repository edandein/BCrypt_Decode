# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: ed
import time
import bcrypt
from multiprocessing import Pool


"""
核心功能
"""
def core(value):
    try:
        hash_value = 'hash'
        check_bc = bcrypt.checkpw(value.encode(), hash_value.encode())
        if check_bc:
            print('\n[★] T: ' + str(value) + ':' + str(hash_value))
            print('\n[★]success[★]')
            exit()
        else:
            print('\n[✰] F: ' + str(value))
        time.sleep(2) # 睡眠一段时间，减小cpu压力
    except Exception as err:
        print(err)


if __name__ == "__main__":
    """
    加载字典
    """
    path = "./passwd.txt"
    with open(path, "r") as f:
        passwd = [i.strip() for i in f.readlines()]
    """
    启用线程池
    """
    pass_pool = Pool(20)
    pass_pool.map(core, passwd)
    pass_pool.close()
    pass_pool.join()