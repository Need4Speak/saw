# Copyright 2016 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

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
        if 'Name' not in update:
            update['Name'] = None
        if 'Action' not in update:
            update['Action'] = None
        if 'Space' in update and update['Space'] is None:
            del update['Space']
        return self.sendtxn('/McTransaction',
                            '/Mc/Transaction',
                            update)

    def create(self, name):
        """
        """
        update = {
            'Action': 'CREATE',
            'Name': name
        }

        return self.send_mc_txn(update)

    def take(self, name, space):
        """
        """
        update = {
            'Action': 'TAKE',
            'Name': name,
            'Space': space,
        }
        return self.send_mc_txn(update)

    def add_patient_info(self, patient_id, patient_name, patient_illness):
        update = {
            "patient_id": patient_id,
            "patient_name": patient_name,
            "patient_illness": patient_illness,
        }
        return self.send_mc_txn(update)
