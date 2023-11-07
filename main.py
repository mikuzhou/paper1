import os
import util.score
import util.find_risk
import util.find_deathlock
import util.generate_code
import util.write_tocsv
import util.fancy_code
import argparse


def find_fancywithdistractor(dlock_num, risk_num, distractor_num):
    file_name1 = "fancy.csv"
    code = util.fancy_code.pythonCodeGenerator(dlock_num, risk_num, distractor_num)
    print(code)
    find_dlock = util.find_deathlock.deadlockAnalyzer(code)
    find_risk = util.find_risk.codeAnalyzer(code)
    need_tobewritten = (util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk), dlock_num, risk_num, distractor_num)
    util.write_to_csv(file_name1, need_tobewritten)
    return util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk);

def find_withoutdistractor(dlock_num, risk_num, distractor_num):
    file_name1 = "without.csv"
    code = util.generate_code.codeGenerator(dlock_num, risk_num, 0)
    find_dlock = util.find_deathlock.deadlockAnalyzer(code)
    find_risk = util.find_risk.codeAnalyzer(code)
    need_tobewritten = (util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk), dlock_num, risk_num, distractor_num)
    util.write_to_csv(file_name1, need_tobewritten)
    return util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk);


def find_withdistractor(dlock_num, risk_num, distractor_num):
    file_name1 = "with.csv"
    code = util.generate_code.codeGenerator(dlock_num, risk_num, distractor_num)
    find_dlock = util.find_deathlock.deadlockAnalyzer(code)
    find_risk = util.find_risk.codeAnalyzer(code)
    need_tobewritten = (util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk), dlock_num, risk_num, distractor_num)
    util.write_to_csv(file_name1, need_tobewritten)
    return util.score.cal_score(dlock_num, risk_num, find_dlock, find_risk);

def main():
    # parser = argparse.ArgumentParser(description="Run specified phases of the grading process.")
    # parser.add_argument('--api_key', default=None,
    #                     help="your api_key")
    # args = parser.parse_args()
    # if args.api_key:
    #     openai_api_key = args.api_key
    i = 0
    while i<10:
        print("new round")
        print(i)
        random_bytes = os.urandom(4)  # 生成4个随机字节
        random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
        dlock_num = random_int % 21
        random_bytes = os.urandom(4)  # 生成4个随机字节
        random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
        risk_num = random_int % 21
        random_bytes = os.urandom(4)  # 生成4个随机字节
        random_int = int.from_bytes(random_bytes, 'big')  # 将字节转换为一个整数
        distractor_num = random_int % 21
        fancy = find_fancywithdistractor(dlock_num, risk_num, distractor_num)
        withC = find_withdistractor(dlock_num, risk_num, distractor_num)
        without = find_withoutdistractor(dlock_num, risk_num, distractor_num)
        print("score")
        print(fancy)
        print(withC)
        print(without)
        i+=1

    # print(util.fancy_code.pythonCodeGenerator(2,3,4))


if __name__ == '__main__':
    main()

