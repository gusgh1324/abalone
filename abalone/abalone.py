import os
import pandas as pd
import numpy as np
from method.win_rate import WinRate

data = pd.read_csv('아발론로그.csv')


# 유저 데이터 저장
def search_user(user):
    user_data = data[data['이름'] == user].values.tolist()
    if user_data:
        return user_data
    else:
        print(f'{user}님의 전적이 존재하지 않습니다')
        os._exit(0)


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

    return zero_data


# 순위랭킹
def win_ranking(unique_names, su, reverse=True):
    wins, win1, win2, win3 = [], [], [], []
    for i in unique_names:
        user_result = data[data['이름'] == i].values.tolist()
        user_name = user_result[0][0]
        wr = WinRate(user_result)
        aa = wr.avg_test()
        if len(aa) >= 3:
            wins.append((aa, user_name))

    wins.sort(key=lambda x: x[0][0], reverse=reverse)
    for win_data in wins:
        win1.append((win_data[0][0], win_data[1]))

    wins.sort(key=lambda x: x[0][1], reverse=reverse)
    for win_data in wins:
        win2.append((win_data[0][1], win_data[1]))

    wins.sort(key=lambda x: x[0][2], reverse=reverse)
    for win_data in wins:
        win3.append((win_data[0][2], win_data[1]))

    print("전체승률")
    for idx, i in enumerate(win1[:su]):
        print(f'{idx + 1}등 {i[1]} {int(i[0])}%')

    print("선승률")
    for idx, i in enumerate(win2[:su]):
        print(f'{idx + 1}등 {i[1]} {int(i[0])}%')

    print("악승률")
    for idx, i in enumerate(win3[:su]):
        print(f'{idx + 1}등 {i[1]} {int(i[0])}%')


# 역순 함수
def win_ranking_re(unique_names, su):
    win_ranking(unique_names, su, reverse=False)


############

###############유저목록###################
unique_names = data['이름'].unique()
print('{:=^90}'.format("유저목록"))
print(f'{unique_names}, 총 {len(unique_names)}명')
##########################################

##########개인 데이터 받아오기###########
user_result = search_user('마레')
user_name = user_result[0][0]

WinRate(user_result).avg_print()
search_job(user_result)

#직업승률
print(search_job(user_result))
##멀린 암살 여부
count_d,count_md = 0,0
for i in user_result:
    if i[1]!='멀린':
        if not pd.isna(i[5]):
            count_d+=(int(i[5]))
    else:
        if not pd.isna(i[5]):
            count_md+=(int(i[5]))


print(f'멀린이 아닐때 암살당한 횟수 {count_d}회')
print(f'멀린일때 암살당한 횟수 {count_md}회')

####################승률 순위####################
# win_ranking(unique_names,3)
# win_ranking_re(unique_names,3)
###############################################

#######게임횟수############
# game_counts = data['게임인원'].value_counts()
# game_all = game_counts.get(7, 0) / 7 + game_counts.get(8, 0)/8 + game_counts.get(9, 0)/9 + game_counts.get(10, 0)/10
# print(f'\r기록된 게임횟수 총 {int(game_all)}판')
##########################

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
#     user_job_data.to_csv(csv_filename)
