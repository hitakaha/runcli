#!/usr/bin/bash
#
# uninstall runcli script

echo "Uninstalling runcli.sh from $NCS_DIR/bin"
rm $NCS_DIR/bin/runcli-dryrun.sh
rm $NCS_DIR/bin/runcli-commit.sh

if [ ! -f $NCS_DIR/bin/runcli-dryrun.sh ] && [ ! -f $NCS_DIR/bin/runcli-commit.sh ]; then
  echo "Successfully uninstalled!"
else
  echo "Failed to uninstall! Please contact the develper."
fi

