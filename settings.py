NUM_RESULTS = 3
MIN_PRICE = 10
MAX_PRICE = 325
SCRAPE_INTERVAL_MINS = 10
CHANNEL = 'pythonaeron'

# Slack token can either be set an an environment var or imported from secrets
# SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Import secret settings (API keys, etc)
try:
    from secrets import *
except Exception:
    pass
