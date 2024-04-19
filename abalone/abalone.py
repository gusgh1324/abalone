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

##############

###############유저목록###################
unique_names = data['이름'].unique()
print('{:=^90}'.format("유저목록"))
print(unique_names, len(unique_names))
##########################################

##########개인 데이터 받아오기###########
user_result = search_user('코더')
user_name = user_result[0][0]
##################################

#############승률계산###############
wr = WinRate(user_result)
wr.avg_print()
###############################

print()

#############직업#################
print(user_name)
search_job(user_result)
#############직업#################