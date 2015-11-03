#!/bin/sh

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

if [ -z "$MOZ_SPLICE_PROD" ]
then
    set -x
    echo "setting up development virtualenv"
    export MOZ_SPLICE_DEV=1
    export CFLAGS='-std=c99'
else
    echo "setting up production virtualenv"
fi

rm -rf splice-env

virtualenv --python=python2.7 --no-site-packages splice-env
. splice-env/bin/activate


python setup.py develop
pip install -r requirements.txt

if [ "$MOZ_SPLICE_DEV" ]
then
    pip install -r requirements-dev.txt
fi
