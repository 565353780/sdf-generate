PROCESSOR_NUM=$2

for i in $(seq 1 ${PROCESSOR_NUM}); do
  python $1 &
  sleep 1
  echo "started Convertor No."$i
done

wait

echo "all Convertors started!"
