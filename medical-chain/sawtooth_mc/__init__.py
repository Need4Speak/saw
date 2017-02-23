import sys
PROJECT_PATH = "../../medical-chain"
SAWTOOTH_CORE_PATH = "../../sawtooth-core"
# The content of sys.path.append is added according to
# sawtooth-core/docs/source/txn_family_tutorial/xo-tutorial-step04/env.sh
sys.path.append("%s/core" % SAWTOOTH_CORE_PATH)
sys.path.append("%s/signing" % SAWTOOTH_CORE_PATH)
sys.path.append("%s/signing/build/lib.linux-x86_64-2.7" % SAWTOOTH_CORE_PATH)
sys.path.append("%s/validator" % SAWTOOTH_CORE_PATH)
sys.path.append("%s/validator/build/lib.linux-x86_64-2.7" % SAWTOOTH_CORE_PATH)
sys.path.append("%s/sdk/python" % SAWTOOTH_CORE_PATH)
sys.path.append(SAWTOOTH_CORE_PATH)
sys.path.append(PROJECT_PATH)

from txn_family import _register_transaction_types

__all__ = [
    'txn_family',
    'xo_cli',
    'xo_client',
    'xo_exceptions'
]


def register_transaction_types(journal):
    _register_transaction_types(journal)