SCRIPT_DIR=$(cd $(dirname $0); pwd)
$SCRIPT_DIR
python3 $SCRIPT_DIR/startAlerm.py
python3 $SCRIPT_DIR/stopAlerm.py
