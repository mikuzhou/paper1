import os
import util.score
import util.find_risk
import util.find_deathlock
import util.generate_code
import util.write_tocsv


def find_withdistractor():
    random_bytes = os.urandom(4)  # 生成4个随机字节
    random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
    dlock_num = random_int % 21
    random_bytes = os.urandom(4)  # 生成4个随机字节
    random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
    risk_num = random_int % 21
    random_bytes = os.urandom(4)  # 生成4个随机字节
    random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
    distractor_num = random_int % 21
    code = util.codeGenerator(dlock_num, risk_num, distractor_num)
    find_dlock = util.deadlockAnalyzer(code)
    find_risk = util.codeAnalyzer(code)
    return util.cal_score(dlock_num, risk_num, find_dlock, find_risk);

def find_withoutdistractor():
    random_bytes = os.urandom(4)  # 生成4个随机字节
    random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
    dlock_num = random_int % 21
    random_bytes = os.urandom(4)  # 生成4个随机字节
    random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
    risk_num = random_int % 21
    code = util.codeGenerator(dlock_num, risk_num, 0)
    find_dlock = util.deadlockAnalyzer(code)
    find_risk = util.codeAnalyzer(code)
    return util.cal_score(dlock_num, risk_num, find_dlock, find_risk)

if __name__ == '__main__':
    file_name1 = "with.csv"
    file_name2 = "without.csv"
    i = 0
    while i<10:
        need_tobewritten = (i,find_withdistractor())
        util.write_to_csv(file_name1, need_tobewritten)
        i+=1
    i = 0
    while i<10:
        need_tobewritten = (i,find_withoutdistractor())
        util.write_to_csv(file_name2, need_tobewritten)
        i+=1

