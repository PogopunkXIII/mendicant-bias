import os
from dotenv import load_dotenv
from logging.config import dictConfig

load_dotenv()

SLACK_API_TOKEN = os.getenv('SLACK_BOT_TOKEN')

LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'formatters': {
      'verbose': {
         'format': '%(levelnames)s %(asctime)s %(module)s %(message)s'
      },
      'simple': {
         'format': '%(levelname)s %(message)s'
      },
   },
   'handlers': {
      'rotate': {
         'level': 'INFO',
         'formatter': 'verbose',
         'class': 'logging.handlers.TimedRotatingFileHandler',
         'filename': os.path.join(PATH, 'logs/mendicant.log'),
         'when': 'midnight',
         'backupCount': '7',
      },
      'slack': {
         'level': 'INFO',
         'api-key': SLACK_API_TOKEN,
         'class': 'slacker_log_handler.SlackerLogHandler',
         'channel': '#logs'
      }
   },
   'loggers': {
      '': {
         'handlers': ['rotate', 'slack'],
         'level': 'INFO'
      }
   }
}
