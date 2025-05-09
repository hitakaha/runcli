#!/usr/bin/env python3
"""
Sample NSO class for runcli package
"""

import requests
from requests.auth import HTTPBasicAuth
import json


class Nso:
    """
    NSO class
    """

    def __init__(
            self, nso_addr="127.0.0.1",
            nso_port="8080",
            username="admin",
            password="admin"
       ):

        self.nso_restconf = f"http://{nso_addr}:{nso_port}/restconf"
        self.headers = {
            'Content-Type':'application/yang-data+json',
            'Accept': 'application/yang-data+json'
        }
        self.auth = HTTPBasicAuth(username, password)


    def exec_cmd(self, device, command):
        """
        execute any commands via live-status/exec/any

        args:
        - device: target device
        - command: command to execute

        return:
        - outputs -> str
        """

        self.url = f"{self.nso_restconf}/operations/tailf-ncs:devices/device={device}/live-status/exec/any"
        self.cmd = command

        self.payload = {
            "input":
            {
                'args': self.cmd
            }
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            auth=self.auth,
            json=self.payload
        )


        # return the outputs, currently works for IOS or IOS-XR NEDs
        if "tailf-ned-cisco-ios-xr-stats:output" in response.json():
            ret = response.json()["tailf-ned-cisco-ios-xr-stats:output"]["result"] 
        elif "tailf-ned-cisco-ios-stats:output" in response.json():
            ret = response.json()["tailf-ned-cisco-ios-stats:output"]["result"] 
        else:
            ret = response.json() # return as it is for other NEDs

        return ret



    def cfg_dryrun(self, device, config):
        """
        sample method to dry-run CLI through RESTCONF, equivalent to following

        $ curl -u admin:admin http://127.0.0.1:8080/restconf/\
            operations/tailf-ncs:devices/runcli:runcli-dryrun \  << runcli-dryrun
            -H 'Content-Type: application/yang-data+json' \
            -X POST -d '{"input": { "device": "R1", "command":"hostname test"}}'

        args:
        - device: target device
        - command: command to execute

        return:
        - outputs -> str
        """

        self.url = f"{self.nso_restconf}/operations/tailf-ncs:devices/runcli:runcli-dryrun"

        self.payload = {
            "input":
            {
                "device": device,
                "command": config
            }
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            auth=self.auth,
            json=self.payload
        )

        return response.json()["runcli:output"]["output"]


    def cfg_commit(self, device, config):
        """
        sample method to commit CLI through RESTCONF, equivalent to following

        [commit]
        $ curl -u admin:admin http://127.0.0.1:8080/restconf/\
            operations/tailf-ncs:devices/runcli:runcli-commit\  << runcli-commit
            -H 'Content-Type: application/yang-data+json' \
            -X POST -d '{"input": { "device": "R1", "command":"hostname test"}}'

        args:
        - device: target device
        - command: command to execute

        return:
        - outputs -> str
        """

        self.url = f"{self.nso_restconf}/operations/tailf-ncs:devices/runcli:runcli-commit"

        self.payload = {
            "input":
            {
                "device": device,
                "command": config
            }
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            auth=self.auth,
            json=self.payload
        )

        return response.json()["runcli:output"]["output"]


if __name__ == "__main__":
    test_nso = Nso("192.168.4.105")

    # execute show users
    output = test_nso.exec_cmd("R1", "show users")

    # define config in text
    new_config = """
router ospf 5
network 1.2.3.4 0.0.0.0 area 0
network 2.3.4.5 0.0.0.0 area 0
    """

    output = test_nso.cfg_dryrun("R1", new_config)
    print(output)
