def solution(schedules, timelogs, startday):
    # 직원들은 일주일동안 자신이 설정한 출근 희망 시각 + 10분까지 어플로 출근해야 합니다.
    # 예를 들어 출근 희망 시각이 9시 58분인 직원은 10시 8분까지 출근해야 합니다. 
    # 단, 토요일, 일요일의 출근 시각은 이벤트에 영향을 끼치지 않습니다. 
    # 직원들은 매일 한 번씩만 어플로 출근하고, 모든 시각은 시에 100을 곱하고 분을 더한 정수로 표현됩니다. 
    # 예를 들어 10시 13분은 1013이 되고 9시 58분은 958이 됩니다.
    # 당신은 직원들이 설정한 출근 희망 시각과 실제로 출근한 기록을 바탕으로 상품을 받을 직원이 몇 명인지 알고 싶습니다.
    
    # 시 = timelog // 100, 분 = timelog % 100 -> divmod(timelog, 100)
    count = 0
    employees = list(zip(schedules, timelogs))
    rest = startday
    
    for schedule, timelog in employees:
        target_h, target_m = divmod(schedule, 100)
        t_full_m = target_h * 60 + target_m
        
        for check in timelog:
            if startday > 5:
                startday += 1
                if startday > 7:
                    startday = 1
                continue
            
            check_h, check_m = divmod(check, 100)
            c_full_m = check_h * 60 + check_m
            if c_full_m > t_full_m + 10:
                startday = rest
                break
            
            startday += 1
        else:
            count += 1
    
    return(count)

