import pandas as pd
from method.win_rate import WinRate

data = pd.read_csv('아발론로그.csv', encoding='cp949')
# 유저 데이터 저장
def search_user(user):
    return data[data['이름'] == user].values.tolist()

### 걸린직업 ###
def job(user_result):
    job_list = [row[1] for row in user_result]
    win_list = [row[2] for row in user_result]
    return job_list,win_list

##########개인 데이터 출력###########
user_result = search_user('코더')
user_name = user_result[0][0]
##################################

#############승률계산###############
wr = WinRate(user_result)
wr.avg_print()
###############################

###############유저목록###################
unique_names = data['이름'].unique()
print('{:=^90}'.format("유저목록"))
print(unique_names, len(unique_names))
##########################################

print()

print(job(user_result)[0])
print(job(user_result)[1])

