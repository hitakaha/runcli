#!/usr/bin/bash
#
# install runcli script

echo "Copying runcli.sh to $NCS_DIR/bin"
cp runcli-dryrun.sh $NCS_DIR/bin
cp runcli-commit.sh $NCS_DIR/bin

if [ -f $NCS_DIR/bin/runcli-dryrun.sh ] && [ -f $NCS_DIR/bin/runcli-commit.sh ]; then
  echo "Successfully installed!"
else
  echo "Failed to install! Please contact the develper."
fi

