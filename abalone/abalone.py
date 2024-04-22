import pandas as pd
import numpy as np
from method.win_rate import WinRate

data = pd.read_csv('아발론로그.csv', encoding='cp949')

# 유저 데이터 저장
def search_user(user):
    return data[data['이름'] == user].values.tolist()

### 걸린직업 ###
def search_job(user_result):
    job_list = ["멀린", "퍼시벌", "시민", "암살자", "모르가나", "모드레드", "오베론", "악세"]
    zero = np.zeros(len(job_list), dtype=int)
    zero_data = pd.DataFrame(zero, index=job_list, columns=['횟수'])
    zero_data['승리'] = 0
    zero_data['패배'] = 0

    for row in user_result:
        job = row[1]
        result = row[2]
        zero_data.loc[job, '횟수'] += 1
        if result == '승리':
            zero_data.loc[job, '승리'] += 1
        elif result == '패배':
            zero_data.loc[job, '패배'] += 1
    print(zero_data)
    return zero_data

#순위랭킹
def win_ranking(unique_names):
    wins, win1, win2, win3 = [], [], [], []
    for i in unique_names:
        user_result = data[data['이름'] == i].values.tolist()
        user_name = user_result[0][0]
        wr = WinRate(user_result)
        aa = wr.avg_test()
        if len(aa) >= 3:
            wins.append((aa, user_name))

    wins.sort(key=lambda x: x[0][0], reverse=True)
    for win_data in wins:
        win1.append((win_data[0][0], win_data[1]))

    wins.sort(key=lambda x: x[0][1], reverse=True)
    for win_data in wins:
        win2.append((win_data[0][1], win_data[1]))

    wins.sort(key=lambda x: x[0][2], reverse=True)
    for win_data in wins:
        win3.append((win_data[0][2], win_data[1]))

    print("전체승률")
    for idx, i in enumerate(win1[:10]):
        print(f'{idx + 1}등 {i[1]} {int(i[0])}%')

    print("선승률")
    for idx, i in enumerate(win2[:10]):
        print(f'{idx + 1}등 {i[1]} {int(i[0])}%')

    print("악승률")
    for idx, i in enumerate(win3[:10]):
        print(f'{idx + 1}등 {i[1]} {int(i[0])}%')
#역순
def win_ranking_re(unique_names):
    wins, win1, win2, win3 = [], [], [], []
    for i in unique_names:
        user_result = data[data['이름'] == i].values.tolist()
        user_name = user_result[0][0]
        wr = WinRate(user_result)
        aa = wr.avg_test()
        if len(aa) >= 3:
            wins.append((aa, user_name))

    wins.sort(key=lambda x: x[0][0])
    for win_data in wins:
        win1.append((win_data[0][0], win_data[1]))

    wins.sort(key=lambda x: x[0][1])
    for win_data in wins:
        win2.append((win_data[0][1], win_data[1]))

    wins.sort(key=lambda x: x[0][2])
    for win_data in wins:
        win3.append((win_data[0][2], win_data[1]))

    print("전체승률")
    for idx, i in enumerate(win1[:10]):
        print(f'{idx + 1}등 {i[1]} {int(i[0])}%')

    print("선승률")
    for idx, i in enumerate(win2[:10]):
        print(f'{idx + 1}등 {i[1]} {int(i[0])}%')

    print("악승률")
    for idx, i in enumerate(win3[:10]):
        print(f'{idx + 1}등 {i[1]} {int(i[0])}%')

############

###############유저목록###################
unique_names = data['이름'].unique()
print('{:=^90}'.format("유저목록"))
print(unique_names, len(unique_names))
##########################################

##########개인 데이터 받아오기###########
user_result = search_user('코더')
user_name = user_result[0][0]

wr = WinRate(user_result)
wr.avg_print()
search_job(user_result)

####################승률 순위####################
win_ranking(unique_names)
win_ranking_re(unique_names)
###############################################

# csv추출
# for i in unique_names:
#     user_result = data[data['이름'] == i].values.tolist()
#     user_name = user_result[0][0]
#     wr = WinRate(user_result)
#     wr.avg_print()
#
#     user_job_data = search_job(user_result)
#
#     csv_filename = f"user_all/{user_name}.csv"
#     user_job_data.to_csv(csv_filename, encoding='utf-8-sig')
