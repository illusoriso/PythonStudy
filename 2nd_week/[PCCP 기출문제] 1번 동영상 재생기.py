# https://school.programmers.co.kr/learn/courses/30/lessons/340213

"""
## 알아야할 함수 ##
- 삼항 연산자 문법 : 값1 if 조건 else 값2

## 특이사항 ##
점수 : 100/100
ez
##################
"""

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_info = []
    # 모두 초단위로 변경
    for x in [video_len, pos, op_start, op_end]:
        a,b = map(int,x.split(':'))
        video_info.append(a*60 + b)
    # 첫 위치가 오프닝 위치에 있는 경우를 위해 한번 해줌
    if video_info[1] >= video_info[2] and video_info[1] <= video_info[3]:
        video_info[1] = video_info[3]
        
    # 입력값에 따라 값 변경
    for command in commands:
        if command == "prev":
            video_info[1] = max(0,video_info[1]-10)
        if command == "next":
            video_info[1] = min(video_info[0],video_info[1]+10)
        if video_info[1] >= video_info[2] and video_info[1] <= video_info[3]:
            video_info[1] = video_info[3]
    # 다시 00:00 형태로 바꿔줌
    mm = video_info[1]//60
    ss = video_info[1]% 60
    answer = ('0'+str(mm) if mm<10  else str(mm))+':'+('0'+str(ss) if ss<10  else str(ss))
    return answer