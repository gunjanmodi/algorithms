def calendar_matching(calendar1, daily_bounds1, calendar2, daily_bounds2, meeting_duration):
    updated_calendar1 = update_calendar(calendar1, daily_bounds1)
    updated_calendar2 = update_calendar(calendar2, daily_bounds2)
    merged_calendar = merge_calendars(updated_calendar1, updated_calendar2)
    flattended_calendar = flatten_calendar(merged_calendar)
    return get_matching_availabilities(flattended_calendar, meeting_duration)


def update_calendar(calendar, daily_bounds):
    new_calendar = calendar[:]
    new_calendar.insert(0, ['0:00', daily_bounds[0]])
    new_calendar.append([ daily_bounds[1], '23:59' ])
    return list(map( lambda m: [time_to_minutes(m[0]), time_to_minutes(m[1])], new_calendar))

def merge_calendars(calendar1, calendar2):
    merged = []
    i, j = 0, 0
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1
    while i < len(calendar1):
        merged.append(calendar1[i])
        i += 1
    while j < len(calendar2):
        merged.append(calendar2[j])
        j += 1
    return merged

def flatten_calendar(calendar):
    flattened = [calendar[0][:]]
    for i in range(1, len(calendar)):
        current = calendar[i]
        previous = flattened[-1]
        current_start, current_end = current
        previous_start, previous_end = previous

        if previous_end >= current_start:
            new_previous = [previous_start, max(current_end, previous_end)]
            flattened[-1] = new_previous
        else:
            flattened.append(current[:])
    print(flattened)
    return flattened

def get_matching_availabilities(calendar, meeting_duration):
    matching_availabilities = []
    for i in range(1, len(calendar)):
        start = calendar[i - 1][1]
        end = calendar[i][0]
        duration = end - start
        if duration >= meeting_duration:
            matching_availabilities.append([start, end])
    # print(matching_availabilities)
    return list(map( lambda m: [ minutes_to_time(m[0]), minutes_to_time(m[1])] ,matching_availabilities))


def time_to_minutes(time):
    hour, minutes = list(map(int, time.split(':')))
    return hour * 60 + minutes

def minutes_to_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    minutes_string = f"0{minutes}" if minutes < 10 else f"{minutes}"
    return f"{hours}:{minutes_string}"
    


if __name__ == '__main__':
    calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
    daily_bounds1 = ["9:00", "20:00"]

    calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
    daily_bounds2 = ["10:00", "18:30"]

    meeting_duration = 30
    output = calendar_matching(calendar1, daily_bounds1, calendar2, daily_bounds2, meeting_duration)
    print(output)


