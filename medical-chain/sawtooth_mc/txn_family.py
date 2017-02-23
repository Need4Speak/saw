import logging

from journal import transaction, global_store_manager
from journal.messages import transaction_message

from sawtooth.exceptions import InvalidTransactionError

LOGGER = logging.getLogger(__name__)


def _register_transaction_types(journal):
    journal.dispatcher.register_message_handler(
        McTransactionMessage,
        transaction_message.transaction_message_handler)
    journal.add_transaction_store(McTransaction)


class McTransactionMessage(transaction_message.TransactionMessage):
    MessageType = "/Mc/Transaction"

    def __init__(self, minfo=None):
        if minfo is None:
            minfo = {}

        super(McTransactionMessage, self).__init__(minfo)

        tinfo = minfo.get('Transaction', {})
        self.Transaction = McTransaction(tinfo)


class McTransaction(transaction.Transaction):
    TransactionTypeName = '/McTransaction'
    TransactionStoreType = global_store_manager.KeyValueStore
    MessageType = McTransactionMessage

    def __init__(self, minfo=None):
        if minfo is None:
            minfo = {}

        super(McTransaction, self).__init__(minfo)

        LOGGER.debug("minfo: %s", repr(minfo))
        LOGGER.error("McTransaction __init__ not implemented")

    def __str__(self):
        LOGGER.error("McTransaction __str__ not implemented")
        return "McTransaction"

    def check_valid(self, store):
        """Determines if the transaction is valid.

         Args:
             store (dict): Transaction store mapping.
         """

        super(McTransaction, self).check_valid(store)

        LOGGER.debug('checking %s', str(self))

        raise InvalidTransactionError('McTransaction.check_valid is not implemented')

    def apply(self, store):
        LOGGER.debug('apply %s', str(self))
        LOGGER.error('McTransaction.apply is not implemented')

    def dump(self):
        result = super(McTransaction, self).dump()

        LOGGER.error('McTransaction.dump is not implemented')

        return result
