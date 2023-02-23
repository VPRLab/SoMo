# SoMo: Beyond “Protected” and “Private”: An Empirical Security Analysis of Custom Function Modifiers in Smart Contracts

## Get Started

### Prerequisites

- We ran our experiments on Ubuntu 20.04 LST OS.
- We used Python 3.10 to develop `SoMo`.
- `SoMo` relies on `slither`, `sold-select`, `networks`, and `z3-solver`. All the essential packages are listed in `requirements.txt`. 

There are steps to locally build `SoMo`.

```shell
git clone git@github.com:VPRLab/SoMo.git && cd SoMo
pip install -r requirements.txt
```

###  Quick Start

`SoMo` takes two arguments, including the contract source code and contract setting.

- Contract source code is usually a file with a `.sol` suffix.
- Contract setting is a `json` file, which contains two essential fields, namely:
  - `ContractName`: which contracts were actually deployed to Ethereum mainnet.
  - `CompilerVersion`: which compilers were used to compile the source code.

Users can specify paths of the source code and setting files by `-c, --code` and `-s, --setting`, respectively.

For instance, there is a vulnerable contract under the `example` folder with its settings.

To validate its security, we can invoke `SoMo` in the following ways.

```shell
python somo -c example/contract.sol -s example/contract.json
```

For more information, please refer to our paper or get help from `python somo -h`.

