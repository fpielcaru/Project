import time, yaml
from datetime import datetime
from db import init_db
from utils.logger import setup_logger
from utils.session_time import is_in_monitoring_window
from collectors.finnhub_collector import get_finnhub_data
from collectors.polygon_collector import get_polygon_data

logger = setup_logger()

with open("config.yaml") as f:
    config = yaml.safe_load(f)

with open("tickers.yaml") as f:
    tickers = yaml.safe_load(f)["tickers"]

conn = init_db(config["database"])
cursor = conn.cursor()

logger.info("Robot pornit")

while True:
    for t in tickers:
        if not t["enabled"]:
            continue

        if not is_in_monitoring_window(
            t["exchange"],
            config["pre_open_minutes"],
            config["post_open_minutes"]
        ):
            continue

        try:
            if t["source"] == "finnhub":
                price, vol = get_finnhub_data(
                    t["symbol"], config["finnhub"]["api_key"]
                )
            else:
                price, vol = get_polygon_data(
                    t["symbol"], config["polygon"]["api_key"]
                )

            cursor.execute(
                "INSERT INTO market_volume VALUES (?,?,?,?,?)",
                (datetime.utcnow().isoformat(), t["symbol"], price, vol, t["source"])
            )
            conn.commit()

            logger.info(f"{t['symbol']} | price={price} | volume={vol}")

        except Exception as e:
            logger.error(f"{t['symbol']} | {e}")

    time.sleep(config["collection_interval_sec"])
