

from sawtooth.client import SawtoothClient


class McClient(SawtoothClient):
    def __init__(self,
                 base_url,
                 keyfile,
                 disable_client_validation=False):
        super(McClient, self).__init__(
            base_url=base_url,
            store_name='McTransaction',
            name='McClient',
            txntype_name='/McTransaction',
            msgtype_name='/Mc/Transaction',
            keyfile=keyfile,
            disable_client_validation=disable_client_validation)

    def send_mc_txn(self, update):
        """
        This sets up the same defaults as the Transaction so when
        signing happens in sendtxn, the same payload is signed.
        Args:
            update: dict The data associated with the Mc data model
        Returns:
            txnid: str The txnid associated with the transaction

        """
        if 'patient_id' not in update:
            update['patient_id'] = None
        if 'patient_name' not in update:
            update['patient_name'] = None
        if 'patient_illness' not in update:
            update['patient_illness'] = None

        return self.sendtxn('/McTransaction',
                            '/Mc/Transaction',
                            update)

    def add_patient_info(self, patient_id, patient_name, patient_illness):
        update = {
            "patient_id": patient_id,
            "patient_name": patient_name,
            "patient_illness": patient_illness,
        }
        return self.send_mc_txn(update)
