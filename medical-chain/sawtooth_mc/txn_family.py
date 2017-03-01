import logging

from journal import transaction, global_store_manager
from journal.messages import transaction_message

from sawtooth.exceptions import InvalidTransactionError

LOGGER = logging.getLogger(__name__)


def _register_transaction_types(journal):
    """Registers the Mc transaction types on the ledger.

    Args:
        ledger (journal.journal_core.Journal): The ledger to register
            the transaction type against.
    """
    journal.dispatcher.register_message_handler(
        McTransactionMessage,
        transaction_message.transaction_message_handler)
    journal.add_transaction_store(McTransaction)


class McTransactionMessage(transaction_message.TransactionMessage):
    """Mc transaction message represent Mc transactions.

    Attributes:
        MessageType (str): The class name of the message.
        Transaction (McTransaction): The transaction the
            message is associated with.
    """
    MessageType = "/Mc/Transaction"

    def __init__(self, minfo=None):
        if minfo is None:
            minfo = {}

        super(McTransactionMessage, self).__init__(minfo)

        tinfo = minfo.get('Transaction', {})
        self.Transaction = McTransaction(tinfo)


class McTransaction(transaction.Transaction):
    """A Transaction is a set of updates to be applied atomically
    to a ledger.

    It has a unique identifier and a signature to validate the source.

    Attributes:
        TransactionTypeName (str): The name of the Xo
            transaction type.
        TransactionTypeStore (type): The type of transaction store.
        MessageType (type): The object type of the message associated
            with this transaction.
    """
    TransactionTypeName = '/McTransaction'
    TransactionStoreType = global_store_manager.KeyValueStore
    MessageType = McTransactionMessage

    def __init__(self, minfo=None):
        """Constructor for the XoTransaction class.

        Args:
            minfo: Dictionary of values for transaction fields.
        """

        if minfo is None:
            minfo = {}

        super(McTransaction, self).__init__(minfo)

        LOGGER.debug("minfo: %s", repr(minfo))
        self._name = minfo['Name'] if 'Name' in minfo else None
        self._action = minfo['Action'] if 'Action' in minfo else None
        self._space = minfo['Space'] if 'Space' in minfo else None

    def __str__(self):
        try:
            oid = self.OriginatorID
        except AssertionError:
            oid = "unknown"
        return "({0} {1} {2})".format(oid,
                                      self._name,
                                      self._space)

    def check_valid(self, store):
        """Determines if the transaction is valid.

         Args:
             store (dict): Transaction store mapping.
         """

        super(McTransaction, self).check_valid(store)

        LOGGER.debug('checking %s', str(self))

        # raise InvalidTransactionError('McTransaction.check_valid is not implemented')
        # pass
        print "Run function check_valid."

    def apply(self, store):
        LOGGER.debug('apply %s', str(self))
        # LOGGER.error('McTransaction.apply is not implemented')
        print "Run function apply"

        if self._name in store:
            game = store[self._name].copy()
        else:
            game = {}

        game["status"] = "1"
        store[self._name] = game

    def dump(self):
        """Returns a dict with attributes from the transaction object.

        Returns:
            dict: The updates from the transaction object.
        """
        result = super(McTransaction, self).dump()

        result['Action'] = self._action
        result['Name'] = self._name
        if self._space is not None:
            result['Space'] = self._space
        LOGGER.info("Run function dump.")
        return result
