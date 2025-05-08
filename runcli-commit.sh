#!/usr/bin/bash
#
# YANG:
#module runcli {
#  namespace "http://com/example/runcli";
#  prefix runcli;
#
#import ietf-inet-types {
#    prefix inet;
#  }
#  import tailf-ncs {
#    prefix ncs;
#  }
#  import tailf-common {
#    prefix tailf;
#  }
#
#  augment /ncs:devices {
#    tailf:action runcli {
#      tailf:exec "runcli.sh";
#      input {
#        leaf device {
#          type string;
#        }
#        leaf command {
#          type string;
#        }
#      }
#
#      output {
#        leaf output {
#          type string;
#        }
#      }
#    } //action
#  } //augment
#}
#
# How to run:
# $ curl -u admin:admin http://127.0.0.1:8080/restconf/operations/tailf-ncs:devices/runcli:runcli -H 'Content-Type: application/yang-data+json' -X POST -d '{"input": { "device": "xr-100", "command":"testtest"}}'
#
# Output:
# {
#  "runcli:output": {
#      "output": "\nyour input is xr-100 command testtest\n"
#        }
# }


result=$({ ncs_cli -u admin << EOF;
switch cli
confi t
devices device $2 config $4
commit
exit no-confirm
exit
EOF
})

echo output '"'
echo "${result}"
echo '"'
