import time
import bcrypt
from multiprocessing import Pool


def decoder(value):
    try:
        hash_value = '$2a$12$1h/shDU9qZCRV/UHhapZI.vwsR4a1sae0VWFUll9fkKgmaT5hVWEa'
        check_bc = bcrypt.checkpw(value.encode(), hash_value.encode())
        if check_bc:
            print('\n[★] T: ' + str(value) + ':' + str(hash_value))
            print('\n[★]success[★]')
            exit()
        else:
            print('\n[✰] F: ' + str(value))
        time.sleep(2)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    path = "E:/工具/fuzzDicts-master/fuzzDicts-master/passwordDict/top500.txt"
    with open("test.txt", "r") as f:
        passwd = [i.strip() for i in f.readlines()]

    pass_pool = Pool(20)
    pass_pool.map(decoder, passwd)
    pass_pool.close()
    pass_pool.join()