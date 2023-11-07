import os
import util.score
import util.find_risk
import util.find_deathlock
import util.generate_code
import util.write_tocsv
import util.fancy_code
import argparse


def find_fancywithdistractor(dlock_num, risk_num, distractor_num):
    code = util.fancy_code.pythonCodeGenerator(dlock_num, risk_num, distractor_num)
    print(code)
    find_dlock = util.find_deathlock.deadlockAnalyzer(code)
    find_risk = util.find_risk.codeAnalyzer(code)
    need_tobewritten = [util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk), dlock_num, risk_num, distractor_num]
    print(util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk))
    return need_tobewritten

def find_withoutdistractor(dlock_num, risk_num, distractor_num):
    code = util.generate_code.codeGenerator(dlock_num, risk_num, 0)
    find_dlock = util.find_deathlock.deadlockAnalyzer(code)
    find_risk = util.find_risk.codeAnalyzer(code)
    need_tobewritten = [util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk), dlock_num, risk_num, 0]
    print(util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk))
    return need_tobewritten


def find_withdistractor(dlock_num, risk_num, distractor_num):
    code = util.generate_code.codeGenerator(dlock_num, risk_num, distractor_num)
    find_dlock = util.find_deathlock.deadlockAnalyzer(code)
    find_risk = util.find_risk.codeAnalyzer(code)
    need_tobewritten = [util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk), dlock_num, risk_num, distractor_num]
    print(util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk))
    return need_tobewritten

def main():
    # parser = argparse.ArgumentParser(description="Run specified phases of the grading process.")
    # parser.add_argument('--api_key', default=None,
    #                     help="your api_key")
    # args = parser.parse_args()
    # if args.api_key:
    #     openai_api_key = args.api_key
    i = 0
    file_name1 = "fancy.csv"
    file_name2 = "without.csv"
    file_name3 = "with.csv"
    fancy_data = []
    without_data = []
    with_data = []
    while i<10:
        print("new round")
        print(i)
        random_bytes = os.urandom(4)  # 生成4个随机字节
        random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
        dlock_num = random_int % 11
        random_bytes = os.urandom(4)  # 生成4个随机字节
        random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
        risk_num = random_int % 11
        random_bytes = os.urandom(4)  # 生成4个随机字节
        random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
        distractor_num = random_int % 11
        fancy_data.append(find_fancywithdistractor(dlock_num, risk_num, distractor_num))
        with_data.append(find_withdistractor(dlock_num, risk_num, distractor_num))
        without_data.append(find_withoutdistractor(dlock_num, risk_num, distractor_num))
        print("score")
        print(fancy_data)
        print(with_data)
        print(without_data)
        i+=1
    util.write_tocsv.write_to_csv(file_name1, fancy_data)
    util.write_tocsv.write_to_csv(file_name2, without_data)
    util.write_tocsv.write_to_csv(file_name3, with_data)

    # print(util.fancy_code.pythonCodeGenerator(2,3,4))


if __name__ == '__main__':
    main()

