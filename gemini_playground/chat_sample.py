import argparse
import google.generativeai as genai
import logging
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

from utils.common_utils import get_env, load_config
from utils.validate_utils import validate_env_name


def setup_logger():
    """
    Logger
    :return:
    """
    # Create logger
    _logger = logging.getLogger("Logger")
    _logger.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Create file handler
    log_file = "./logs/chat_sample_{}.log".format(timestamp)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    _logger.addHandler(file_handler)

    # Create console_handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    _logger.addHandler(console_handler)

    return _logger


def execute():
    """
    Execute
    :return:
    """
    genai.configure(api_key=get_env("GOOGLE_API_KEY"))
    # model = genai.GenerativeModel(conf["model_flash"])
    model = genai.GenerativeModel(conf["model_pro"])
    chat = model.start_chat(history=[])

    while True:
        message = input("Please enter your question : ")
        if message == "exit":
            logger.info("Process terminated.")
            break
        response = chat.send_message(message)
        print("Answer : ")
        print(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--env", type=validate_env_name, required=True, help="Environment to be updated"
    )
    args = parser.parse_args()
    env = args.env.lower()

    # 환경변수 로드
    load_dotenv(verbose=True)
    load_dotenv(f"envs/.{env}.env", override=True)

    # Config
    conf = load_config()

    # 글로벌 변수로 Logger 를 만들어 두기
    now = datetime.now(ZoneInfo("Asia/Tokyo"))
    timestamp = now.strftime("%Y%m%d%H%M%S")
    logger = setup_logger()
    logger.info(f"Processing {env} environment")

    execute()
