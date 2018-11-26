from eth.constants import (
    ZERO_ADDRESS,
)
from eth.beacon.state_machines.configs import BeaconConfig


SERENITY_CONFIG = BeaconConfig(
    SHARD_COUNT=2**10,  # = 1,024 shards
    DEPOSIT_SIZE=2**5,  # = 32 ETH
    MIN_ONLINE_DEPOSIT_SIZE=2**4,  # = 16 ETH
    DEPOSIT_CONTRACT_ADDRESS=ZERO_ADDRESS,  # TODO: TBD
    TARGET_COMMITTEE_SIZE=2**8,  # = 256 validators
    SLOT_DURATION=6,  # seconds
    CYCLE_LENGTH=2**6,  # = 64 slots
    MIN_VALIDATOR_SET_CHANGE_INTERVAL=2**8,  # = 256 slots
    SHARD_PERSISTENT_COMMITTEE_CHANGE_PERIOD=2**17,  # = 131,072 slots
    MIN_ATTESTATION_INCLUSION_DELAY=2**2,  # = 4 slots
    SQRT_E_DROP_TIME=2**18,  # = 262,144 slots
    WITHDRAWALS_PER_CYCLE=2**2,  # = 4 validators
    MIN_WITHDRAWAL_PERIOD=2**13,  # = 8,192 slots
    DELETION_PERIOD=2**22,  # = 4,194,304 slots
    COLLECTIVE_PENALTY_CALCULATION_PERIOD=2**20,  # = 1,048,576 slots
    POW_RECEIPT_ROOT_VOTING_PERIOD=2**10,  # = 1024
    SLASHING_WHISTLEBLOWER_REWARD_DENOMINATOR=2**9,  # = 512
    BASE_REWARD_QUOTIENT=2**15,  # = 32,768
    MAX_VALIDATOR_CHURN_QUOTIENT=2**5,  # = 32
    POW_CONTRACT_MERKLE_TREE_DEPTH=2**5,  # =32
    MAX_ATTESTATION_COUNT=2**7,  # 128
    INITIAL_FORK_VERSION=0,
)
