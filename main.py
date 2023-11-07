import os
import util.score
import util.find_risk
import util.find_deathlock
import util.generate_code
import util.write_tocsv
import util.fancy_code
import argparse
import openai


def find_fancywithdistractor():
    random_bytes = os.urandom(4)  # 生成4个随机字节
    random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
    dlock_num = random_int % 21
    random_bytes = os.urandom(4)  # 生成4个随机字节
    random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
    risk_num = random_int % 21
    random_bytes = os.urandom(4)  # 生成4个随机字节
    random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
    distractor_num = random_int % 21
    code = util.fancy_code.pythonCodeGenerator(dlock_num, risk_num, distractor_num)
    find_dlock = util.find_deathlock.deadlockAnalyzer(code)
    find_risk = util.find_risk.codeAnalyzer(code)
    return util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk);

def find_withoutdistractor():
    random_bytes = os.urandom(4)  # 生成4个随机字节
    random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
    dlock_num = random_int % 21
    random_bytes = os.urandom(4)  # 生成4个随机字节
    random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
    risk_num = random_int % 21
    code = util.generate_code.codeGenerator(dlock_num, risk_num, 0)
    find_dlock = util.find_deathlock.deadlockAnalyzer(code)
    find_risk = util.find_risk.codeAnalyzer(code)
    return util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk);


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
    code = util.generate_code.codeGenerator(dlock_num, risk_num, distractor_num)
    find_dlock = util.find_deathlock.deadlockAnalyzer(code)
    find_risk = util.find_risk.codeAnalyzer(code)
    return util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk);

def main():
    # parser = argparse.ArgumentParser(description="Run specified phases of the grading process.")
    # parser.add_argument('--api_key', default=None,
    #                     help="your api_key")
    # args = parser.parse_args()
    # if args.api_key:
    #     openai_api_key = args.api_key
    # file_name1 = "with.csv"
    # file_name2 = "without.csv"
    # file_name3 = "fancy.csv"
    # i = 0
    # while i<10:
    #     need_tobewritten = (i,find_withdistractor())
    #     util.write_to_csv(file_name1, need_tobewritten)
    #     i+=1
    # i = 0
    # while i<10:
    #     need_tobewritten = (i,find_withoutdistractor())
    #     util.write_to_csv(file_name2, need_tobewritten)
    #     i+=1
    # i = 0
    # while i<10:
    #     need_tobewritten = (i,find_withoutdistractor())
    #     util.write_to_csv(file_name3, need_tobewritten)
    #     i+=1
    print(util.fancy_code.pythonCodeGenerator(2,3,4))


if __name__ == '__main__':
    main()

