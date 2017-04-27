import logging

from journal import transaction, global_store_manager
from journal.messages import transaction_message

from sawtooth.exceptions import InvalidTransactionError

LOGGER = logging.getLogger(__name__)


def _register_transaction_types(journal):
    """Registers the Ac transaction types on the ledger.

    Args:
        ledger (journal.journal_core.Journal): The ledger to register
            the transaction type against.
    """
    journal.dispatcher.register_message_handler(
        AcTransactionMessage,
        transaction_message.transaction_message_handler)
    journal.add_transaction_store(AcTransaction)


class AcTransactionMessage(transaction_message.TransactionMessage):
    """Ac transaction message represent Ac transactions.

    Attributes:
        MessageType (str): The class name of the message.
        Transaction (AcTransaction): The transaction the
            message is associated with.
    """
    MessageType = "/Ac/Transaction"

    def __init__(self, minfo=None):
        if minfo is None:
            minfo = {}

        super(AcTransactionMessage, self).__init__(minfo)

        tinfo = minfo.get('Transaction', {})
        self.Transaction = AcTransaction(tinfo)


class AcTransaction(transaction.Transaction):
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
    TransactionTypeName = '/AcTransaction'
    TransactionStoreType = global_store_manager.KeyValueStore
    MessageType = AcTransactionMessage

    def __init__(self, minfo=None):
        """Constructor for the XoTransaction class.

        Args:
            minfo: Dictionary of values for transaction fields.
        """

        if minfo is None:
            minfo = {}

        super(AcTransaction, self).__init__(minfo)

        LOGGER.debug("minfo: %s", repr(minfo))
        self._patient_id = minfo['patient_id'] if 'patient_id' in minfo else None
        self._patient_name = minfo['patient_name'] if 'patient_name' in minfo else None
        self._patient_illness = minfo['patient_illness'] if 'patient_illness' in minfo else None

    def __str__(self):
        try:
            oid = self.OriginatorID
        except AssertionError:
            oid = "unknown"
        return "({0} {1} {2})".format(oid,
                                      self._patient_id,
                                      self._patient_illness)

    def check_valid(self, store):
        """Determines if the transaction is valid.

         Args:
             store (dict): Transaction store mapping.
         """

        super(AcTransaction, self).check_valid(store)

        LOGGER.debug('checking %s', str(self))

        # raise InvalidTransactionError('AcTransaction.check_valid is not implemented')
        # pass
        print "Run function check_valid."

    def apply(self, store):
        LOGGER.debug('apply %s', str(self))
        # LOGGER.error('AcTransaction.apply is not implemented')
        print "Run function apply"

        if self._patient_id in store:
            game = store[self._patient_id].copy()
        else:
            game = {}

        game["status"] = "1"
        store[self._patient_id] = game

    def dump(self):
        """Returns a dict with attributes from the transaction object.

        Returns:
            dict: The updates from the transaction object.
        """
        result = super(AcTransaction, self).dump()

        result['patient_name'] = self._patient_name
        result['patient_id'] = self._patient_id
        result['patient_illness'] = self._patient_illness

        return result
