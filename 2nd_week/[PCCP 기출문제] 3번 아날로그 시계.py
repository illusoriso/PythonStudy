# https://school.programmers.co.kr/learn/courses/30/lessons/250135

"""
## 알아야할 함수 ##
- 파이썬 줄 바꿈 : \ (백슬래쉬)

## 특이사항 ##
점수 : /100
##################
"""


prinprint_flag = 0

def solution(h1, m1, s1, h2, m2, s2):
    # h1, m1, s1, h2, m2, s2 = 	11, 58, 59, 11, 59, 0
    answer = 0
    #초단위로 변환
    start_time = h1*3600+m1*60+s1
    end_time = h2*3600+m2*60+s2
    if print_flag:
        print(f'start_time : {start_time}')
        print(f'end_time : {end_time}')
    
    #각속도 계산
    hour_vel = 30/3600 # 30/3600 deg/s
    min_vel = 0.1      # 360/3600 deg/s
    sec_vel = 6        # 360/60 deg/s
    
    hour_oncoming_flag, min_oncoming_flag = 0,0
    rounded_hour_pos, rounded_minute_pos = -1,-1
    
    #시작시간부터 종료시간까지
    for time in range(start_time, end_time+1):
        # 각 시간별 침 위치 계산
        hour_pos = (time * hour_vel) % 360
        minute_pos = (time * min_vel) % 360
        second_pos = (time * sec_vel) % 360
        
        #세개 다 겹칠경우 계산
        if (time == 0 or time == 3600*12):
            if print_flag:
                print(f'세개 다 겹쳐!!')
                print(f'{time//3600}시 {time%3600//60}분 {time%3600%60}초!!')
            answer += 1
            continue
        
        # exact second에 겹치는 경우 계산
        if hour_pos == second_pos or minute_pos == second_pos:
            if print_flag:
                print(f'정초에 겹쳐!!')
                print(f'{time//3600}시 {time%3600//60}분 {time%3600%60}초!!')
            answer += 1
            continue
        
        # 애매하게 겹치는 경우 계산
        if hour_pos % 6 != 0:
            rounded_hour_pos = ((hour_pos//6)+1)*6 % 360
        else:
            rounded_hour_pos = hour_pos
        if minute_pos % 6 != 0:
            rounded_minute_pos = ((minute_pos//6)+1)*6 % 360
        else:
            rounded_minute_pos = minute_pos
        
        # 이전 스텝에 플래그가 올라갔고, 시/분침을 round한 값과 초침이 같은 위치에 있다면 더해주기
        if hour_oncoming_flag:
            if print_flag:
                print('이전스텝에 플래그(시) 올라감!')
            if rounded_hour_pos == second_pos:
                if print_flag:
                    print(f'시침과 애매하게 겹쳤었어!!')
                    print(f'{time//3600}시 {time%3600//60}분 {time%3600%60}초!!')
                answer+= 1
        
        if min_oncoming_flag:
            if print_flag:
                print('이전스텝에 플래그(분) 올라감!')
            if rounded_minute_pos == second_pos:
                if print_flag:
                    print(f'분침과 애매하게 겹쳤었어!!')
                    print(f'{time//3600}시 {time%3600//60}분 {time%3600%60}초!!')
                answer+= 1
                
        # 플래그 관리 (특정 시점 이후 1초 안에 겹친다는 플래그를 올려줌)
        if rounded_hour_pos == (second_pos + 6)%360:
            if print_flag:
                print(f'시침이 다가오고 있어!!')
                print(f'{time//3600}시 {time%3600//60}분 {time%3600%60}초!!')
            hour_oncoming_flag = 1
        else:
            hour_oncoming_flag = 0
            
        if rounded_minute_pos == (second_pos + 6)%360:
            if print_flag:
                print(f'분침이 다가오고 있어!!')
                print(f'{time//3600}시 {time%3600//60}분 {time%3600%60}초!!')
            min_oncoming_flag = 1
        else:
            min_oncoming_flag = 0
        
    
    return answer