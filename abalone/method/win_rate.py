class WinRate:
    def __init__(self, user_result):
        self.user_result = user_result

    def avg_run_all(self):
        count_avg_all = []
        count_avg_all.append(self.avg_winrate())
        count_avg_all.append(self.avg_winrate_evil())
        count_avg_all.append(self.avg_winrate_good())

        return count_avg_all

    def avg_winrate(self):
        win_count = sum('승리' in sublist for sublist in self.user_result)
        loss_count = sum('패배' in sublist for sublist in self.user_result)
        total_count = len(self.user_result)
        return [win_count, loss_count, total_count]

    def avg_winrate_evil(self):
        win_count = sum(sublist[2] == '승리' and sublist[8] == '선' for sublist in self.user_result)
        loss_count = sum(sublist[2] == '패배' and sublist[8] == '선' for sublist in self.user_result)
        total_count = win_count + loss_count
        return [win_count, loss_count, total_count]

    def avg_winrate_good(self):
        win_count = sum(sublist[2] == '승리' and sublist[8] == '악' for sublist in self.user_result)
        loss_count = sum(sublist[2] == '패배' and sublist[8] == '악' for sublist in self.user_result)
        total_count = win_count + loss_count
        return [win_count, loss_count, total_count]

    def avg_print(self):
        user_avg = self.avg_run_all()
        print(f'{self.user_result[0][0]} 승률')
        char = ["전체승률", "선 승률", "악 승률"]
        for title, data in zip(char, user_avg):
            print('{:=^20}'.format(title))
            win_rate = (data[0] / data[2]) * 100
            print(f'{data[2]}전 {data[0]}승 {data[1]}패')
            print(f' {win_rate:.1f}%')