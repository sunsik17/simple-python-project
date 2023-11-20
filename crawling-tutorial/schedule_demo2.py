import schedule
import time


def message(interval):
    print(f'{interval} 간격 스케줄 실행중.. ')


schedule.every(5).seconds.do(message, '5초')

count = 0
while True:
    schedule.run_pending()
    time.sleep(5)
    count += 1
    if count == 2:
        break

schedule.clear()

job = schedule.every(1).seconds.do(message, '1초')
count = 0
while count < 5:
    schedule.run_pending()
    time.sleep(1)
    count += 1

schedule.cancel_job(job)
print(f'{count}초 경과 스케줄 종료')