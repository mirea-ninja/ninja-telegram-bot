from envparse import env

TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN", default="")
SENTRY_URL = env.str("SENTRY_URL", default="")
POSTGRES_URI = env.str(
    "POSTGRES_URI", default="postgres://postgres:oniel@localhost/postgres")
MIREA_NINJA_GROUP_ID = env.int("MIREA_NINJA_GROUP_ID", default=-567317308)
YANDEX_API_KEY = env.str("YANDEX_API_KEY", default="")
YANDEX_WEATHER_API_KEY = env.str("YANDEX_WEATHER_API_KEY", default="")
YANDEX_FOLDER_ID = env.str("YANDEX_FOLDER_ID", default="")