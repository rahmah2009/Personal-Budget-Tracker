import datetime

def get_date():
    today = datetime.date.today()
    result = today.isoformat()
    return result