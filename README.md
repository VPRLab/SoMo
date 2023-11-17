# SoMo: Beyond “Protected” and “Private”: An Empirical Security Analysis of Custom Function Modifiers in Smart Contracts

## Overview

`SoMo` is the implementation of the paper titled *"SoMo: Beyond “Protected” and “Private”: An Empirical Security Analysis of Custom Function Modifiers in Smart Contracts"* published on "ISSTA'23", which has been integrated into [MetaScan](https://metatrust.io/metascan) services hosted at [MetaTrustLab](https://github.com/MetaTrustLabs). `SoMo` is a static analyzer designed for detecting **<u>bypassable</u>** `modifier` in `Solidity` smart contracts based on taint analysis and [Slither](https://github.com/crytic/slither).

## Usage

You can find the ISSTA paper via this [link](https://daoyuan14.github.io/papers/ISSTA23_SoMo.pdf) and please consider citing our paper if it's useful to you.

```latex
@INPROCEEDINGS{SoMo2023,
  author = {Fang, Yuzhou and Wu, Daoyuan and Yi, Xiao and Wang, Shuai and Chen, Yufan and Chen, Mengjie and Liu, Yang and Jiang, Lingxiao},
  booktitle = {Proc. ACM ISSTA},
  title = {Beyond ``Protected'' and ``Private'': An Empirical Security Analysis of Custom Function Modifiers in Smart Contracts (To appear)},
  year = {2023}
}
```

MetaTrustLab hosts another version of `SoMo` running on [MetaScan](https://metatrust.io/metascan), and the code is available in [falcon](https://github.com/MetaTrustLabs/falcon-metatrust/tree/main/falcon/somo).

For the dataset used in the paper, please refer to the dataset repository at [VPRLab/ModifierDataset](https://github.com/VPRLab/ModifierDataset).

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

To detect the bypassable modifiers, users can invoke `SoMo` in the following instruction.

```shell
python somo -c example/contract.sol -s example/contract.json
```

For more information, please refer to our paper or get help from `python somo -h`.

