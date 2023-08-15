"""Enum containing the different Transaction types."""

from enum import Enum


class TransactionType(str, Enum):
    """Enum containing the different Transaction types."""

    ACCOUNT_DELETE = "AccountDelete"
    ACCOUNT_SET = "AccountSet"
    CHECK_CANCEL = "CheckCancel"
    CHECK_CASH = "CheckCash"
    CHECK_CREATE = "CheckCreate"
    CLAWBACK = "Clawback"
    DEPOSIT_PREAUTH = "DepositPreauth"
    ESCROW_CANCEL = "EscrowCancel"
    ESCROW_CREATE = "EscrowCreate"
    ESCROW_FINISH = "EscrowFinish"
    NFTOKEN_ACCEPT_OFFER = "NFTokenAcceptOffer"
    NFTOKEN_BURN = "NFTokenBurn"
    NFTOKEN_CANCEL_OFFER = "NFTokenCancelOffer"
    NFTOKEN_CREATE_OFFER = "NFTokenCreateOffer"
    NFTOKEN_MINT = "NFTokenMint"
    OFFER_CANCEL = "OfferCancel"
    OFFER_CREATE = "OfferCreate"
    PAYMENT = "Payment"
    PAYMENT_CHANNEL_CLAIM = "PaymentChannelClaim"
    PAYMENT_CHANNEL_CREATE = "PaymentChannelCreate"
    PAYMENT_CHANNEL_FUND = "PaymentChannelFund"
    SET_REGULAR_KEY = "SetRegularKey"
    SIGNER_LIST_SET = "SignerListSet"
    TICKET_CREATE = "TicketCreate"
    TRUST_SET = "TrustSet"
    XCHAIN_ACCOUNT_CREATE_COMMIT = "XChainAccountCreateCommit"
    XCHAIN_ADD_ACCOUNT_CREATE_ATTESTATION = "XChainAddAccountCreateAttestation"
    XCHAIN_ADD_CLAIM_ATTESTATION = "XChainAddClaimAttestation"
    XCHAIN_CLAIM = "XChainClaim"
    XCHAIN_COMMIT = "XChainCommit"
    XCHAIN_CREATE_BRIDGE = "XChainCreateBridge"
    XCHAIN_CREATE_CLAIM_ID = "XChainCreateClaimID"
    XCHAIN_MODIFY_BRIDGE = "XChainModifyBridge"
