import os
import argparse
import subprocess
from solmoctor.core import SlitherParser
from solmoctor.solmoctor import SolMoctor


class SoMoRun:
    def __init__(self) -> None:
        self.args = self._get_args()
        self.solc_select, self.solc = self._get_solc()
        self.parser: SlitherParser = SlitherParser(self.solc)
        self.somo = SolMoctor()
    
    def _get_solc(self) -> str:
        # Obtain essential components relying on.
        result = subprocess.run(["which", "solc-select"], stdout=subprocess.PIPE)
        if result.returncode != 0:
            print("Error: Can not find `solc-select`.")
            exit(-1)
        solc_select = result.stdout.decode("utf-8").replace("\n", "")
        
        result = subprocess.run(["which", "solc"], stdout=subprocess.PIPE)
        if result.returncode != 0:
            print("Error: Can not find `solc`.")
            exit(-1)
        solc = result.stdout.decode("utf-8").replace("\n", "")

        return solc_select, solc
    
    def _get_args(self):
        # Create a new ArgumentParser object
        parser = argparse.ArgumentParser(description='SoMo ArgParser')

        # Add an argument for the input file
        parser.add_argument( '-c', '--code', type=str, required=True, help='Input contract source code.')

        # Add an optional argument for the output file
        parser.add_argument( '-s', '--setting', type=str, required=True, help='Input contract settings.')

        # Parse the command line arguments
        return parser.parse_args()
    
    def run(self):
        # parse the contract first
        contract, slither = self.parser.parse(self.args.code, self.args.setting)
        status, result = self.somo.check(contract, slither)
        print(status)
        print(result)


if __name__ == '__main__':
    SoMoRun().run()
