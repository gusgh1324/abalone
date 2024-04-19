############### 승률 #################
# 승률 데이터 저장
def avg_run_all(user_result):
    count_avg_all = []
    count_avg_all.append(avg_winrate(user_result))
    count_avg_all.append(avg_winrate_evil(user_result))
    count_avg_all.append(avg_winrate_good(user_result))

    return count_avg_all
# 전체 승률
def avg_winrate(user_result):
    avg_winrate = []
    avg_winrate.append(sum('승리' in sublist for sublist in user_result))
    avg_winrate.append(sum('패배' in sublist for sublist in user_result))
    avg_winrate.append(len(user_result))

    return avg_winrate
# 악 승률
def avg_winrate_evil(user_result):
    avg_winrate_evil = []
    avg_winrate_evil.append(sum(sublist[2] == '승리' and sublist[8] == '선' for sublist in user_result))
    avg_winrate_evil.append(sum(sublist[2] == '패배' and sublist[8] == '선' for sublist in user_result))
    avg_winrate_evil.append(sum(avg_winrate_evil))
    return avg_winrate_evil
# 선승률
def avg_winrate_good(user_result):
    avg_winrate_good = []
    avg_winrate_good.append(sum(sublist[2] == '승리' and sublist[8] == '악' for sublist in user_result))
    avg_winrate_good.append(sum(sublist[2] == '패배' and sublist[8] == '악' for sublist in user_result))
    avg_winrate_good.append(sum(avg_winrate_good))
    return avg_winrate_good
# 승률 텍스트 출력
def avg_print(list,user_name):
    print(f'{user_name} 승률')
    char = ["전체승률", "선 승률", "악 승률"]
    for title, i in zip(char, list):
        print('{:=^20}'.format(title))
        print(f'{i[2]}전 {i[0]}승 {i[1]}패')
        win_rate = (i[0] / i[2]) * 100
        print(f' {win_rate:.1f}%')
############### 승률 #################