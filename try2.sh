if [ ! -d "/sys/class/gpio/gpio24" ]; then
echo 24 > /sys/class/gpio/export
echo out >  /sys/class/gpio/gpio24/direction
echo 1 >  /sys/class/gpio/gpio24/value
fi

while true
do
echo 0 >  /sys/class/gpio/gpio24/value
sleep 0.05
echo 1 >  /sys/class/gpio/gpio24/value
sleep 0.05
echo 0 >  /sys/class/gpio/gpio24/value
sleep 0.05
echo 1 >  /sys/class/gpio/gpio24/value
sleep 0.05
echo 0 >  /sys/class/gpio/gpio24/value
sleep 0.05
echo 1 >  /sys/class/gpio/gpio24/value
sleep 0.05




sleep 5
done
