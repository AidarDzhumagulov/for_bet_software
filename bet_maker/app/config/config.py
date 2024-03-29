import os
import sys

import yaml


API_CONFIGS_DIR = "config/app.configs/"
COMMON_CONFIGS_DIR = "config/common"


if os.environ.get("config"):
    CONFIG_FILE = os.environ.get("config")


config = {}


def extend_config(configs_dir):
    configs_list = os.listdir(configs_dir)
    for config_filename in configs_list:
        config_path = os.path.join(configs_dir, config_filename)

        with open(config_path, "r") as yml_file:
            data = yaml.load(yml_file, Loader=yaml.FullLoader)
            if data:
                config.update(data)


try:
    extend_config(API_CONFIGS_DIR)
    extend_config(COMMON_CONFIGS_DIR)


except FileNotFoundError:
    sys.exit(os.EX_CONFIG)
