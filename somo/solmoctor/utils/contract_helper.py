# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 19:30
# @Author  : CharesFang

# To read auxiliary information to help compile contracts into Slither obj.

import re
import json
from typing import Dict
from solmoctor.exception import ContractVersionNotFound


class ContractHelper:
    def __init__(self, setting_path: str):
        self.version_pattern = re.compile(r'0.[1-9].\d{1,2}')
        self.contract_setting = self.read_setting(setting_path)

    @staticmethod
    def read_setting(setting_path: str) -> Dict:
        with open(setting_path, "r") as file:
            return json.load(file)

    @property
    def main_contract(self):
        return self.contract_setting['ContractName']

    @property
    def compiler_version(self):
        res = self.version_pattern.search(self.contract_setting['CompilerVersion'])
        if res:
            return res.group()
        else:
            raise ContractVersionNotFound(f"{self.contract}: can not get compiler version.")
