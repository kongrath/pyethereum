import copy
from ethereum import utils, config
from ethereum.tools.tester import a0

casper_config = dict(
    # The Casper-specific config declaration
    METROPOLIS_FORK_BLKNUM=0,
    ANTI_DOS_FORK_BLKNUM=0,
    CLEARING_FORK_BLKNUM=0,
    CONSENSUS_STRATEGY='hybrid_casper',
    NULL_SENDER=b'\xff' * 32,
    EPOCH_LENGTH=50,
    NON_REVERT_MIN_DEPOSIT=10**18,
    OWNER=a0
)

config.casper_config = {**config.default_config, **casper_config}
