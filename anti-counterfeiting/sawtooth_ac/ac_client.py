

from sawtooth.client import SawtoothClient


class AcClient(SawtoothClient):
    def __init__(self,
                 base_url,
                 keyfile,
                 disable_client_validation=False):
        super(AcClient, self).__init__(
            base_url=base_url,
            store_name='AcTransaction',
            name='AcClient',
            txntype_name='/AcTransaction',
            msgtype_name='/Ac/Transaction',
            keyfile=keyfile,
            disable_client_validation=disable_client_validation)

    def send_ac_txn(self, update):
        """
        This sets up the same defaults as the Transaction so when
        signing happens in sendtxn, the same payload is signed.
        Args:
            update: dict The data associated with the Ac data model
        Returns:
            txnid: str The txnid associated with the transaction

        """
        if 'patient_id' not in update:
            update['patient_id'] = None
        if 'patient_name' not in update:
            update['patient_name'] = None
        if 'patient_illness' not in update:
            update['patient_illness'] = None

        return self.sendtxn('/AcTransaction',
                            '/Ac/Transaction',
                            update)

    def add_patient_info(self, patient_id, patient_name, patient_illness):
        update = {
            "patient_id": patient_id,
            "patient_name": patient_name,
            "patient_illness": patient_illness,
        }
        return self.send_ac_txn(update)
