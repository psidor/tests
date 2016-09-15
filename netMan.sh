ROUTER1=192.168.1.1
ROUTER2=192.168.7.1

ping -c 2 $ROUTER1
connected=$?
#if net is down then restart and reboot
if [ $connected -ne 0 ];then

ping -c 2 $ROUTER2
connected=$?
if [ $connected -ne 0 ];then
echo "network is not very well !"
echo "restart network"

/etc/init.d/networking restart
/sbin/ifdown wlan0
/sbin/ifup wlan0

fi
fi


