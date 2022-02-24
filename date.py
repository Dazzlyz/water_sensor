from datetime import datetime

def get_date():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return date

