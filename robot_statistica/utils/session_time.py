from datetime import datetime, time, timedelta
import pytz

SESSIONS = {
    "NASDAQ": (time(9, 30), pytz.timezone("US/Eastern")),
    "FOREX":  (time(0, 0), pytz.utc),
}

def is_in_monitoring_window(exchange, pre_minutes, post_minutes):
    open_time, tz = SESSIONS[exchange]
    now = datetime.now(tz)

    session_open = now.replace(
        hour=open_time.hour,
        minute=open_time.minute,
        second=0,
        microsecond=0
    )

    start = session_open - timedelta(minutes=pre_minutes)
    end = session_open + timedelta(minutes=post_minutes)

    return start <= now <= end
