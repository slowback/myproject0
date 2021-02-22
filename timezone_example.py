
import datetime
import pytz
import random

while True:
    print('--- select time zone ---')
    i = input('enter amount time zone: ')

    if not i.isdigit():
        continue

    if int(i) == 0:
        break
    else:

        i = int(i)

        list_random = [random.choice(sorted(pytz.country_names)) for _ in range(i)]
        for x in list_random:
            print('{}: {}: {}'.format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

        i_tz = input('Please select tim zone: ')

        utc_time = datetime.datetime.utcnow()

        aware_local_time = pytz.utc.localize(utc_time).astimezone()
        aware_utc_time = pytz.utc.localize(utc_time)

        select = 0

        if len(pytz.country_timezones(i_tz)) > 1:
            # print(' {}'.format(pytz.country_timezones.get(i_tz)))
            print([f'{i + 1}: {v}' for i, v in enumerate(pytz.country_timezones.get(i_tz))])
            select = int(input(f'select 1 - {len(pytz.country_timezones(i_tz))}: '))
            # print('your select {}, time zone is {}'.format(i_tz, pytz.country_timezones(i_tz[select])))

        country = pytz.country_timezones.get(i_tz)
        s = country[select - 1]
        # print(s)

        tz_to_display = pytz.timezone(s)
        local_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {}".format(s, local_time))
