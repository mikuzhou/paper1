def cal_score(x1, x2, y1, y2):
    if x1 != 0 and x2 != 0:
        return 100.0 - abs(y1-x1) / x1 * 50.0 - abs(y2-x2) / x2 * 50.0
    elif x1 == 0 and x2!=0:
        return 100.0 - abs(y2-x2) / x2 * 100.0
    elif x1 != 0 and x2 == 0:
        return 100.0 - abs(y1-x1) / x1 * 100.0
    else:
        if y1!=0 and y2!=0:
            return 0.0
        elif y1==0 and y2==0:
            return 100.0
        else:
            return 50.0
