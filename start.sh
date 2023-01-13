export ALGORITHM_ENV=$1


time=$(date "+%Y-%m-%d-%H-%M-%S")

nohup python service.py >$1-$time.log 2>&1 &

#port=8888
#nohup gunicorn -w 1 -b 0.0.0.0:$port service:app --timeout 1000 >$1-$time.log 2>&1 &