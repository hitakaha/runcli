runcli package README

-----------------------
1. Introduction
-----------------------

  This document describes how to use runcli package.
  The purpose of this package is to run CLI commands via RESTCONF.


-----------------------
2. Getting started
-----------------------

  To use this package, you have to execute "install.sh" first.
  The script copies the necessary files to $NCS_DIR.

  Following is sample output.

  $ ./install.sh 
  Copying runcli.sh to NSO-6.1.2/bin
  Successfully installed!


-----------------------
3. How to use
-----------------------

  Now, you can use RESTCONF to execute cli, such as follows.

  $ curl -u admin:admin http://127.0.0.1:8080/restconf/operations/tailf-ncs:devices/runcli:runcli -H 'Content-Type: application/yang-data+json' -X POST -d $'{"input": { "device": "R1", "command":"testtest"}}'



-----------------------
4. Troubleshoot
-----------------------

  This package simply calls scripts via Action.
  If it does not work, check the script works on the NSO server.

  To test the script itself, use following CLI.
  $ $NCS_DIR/bin/runcli-dryrun.sh "device" "R1" "command" "testtest"


-----------------------
5. END OF README FILE
-----------------------
