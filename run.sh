#!/usr/bin/env bash
if [[ "$(docker images -q check-orders:0.0.1 2> /dev/null)" == "" ]]; then
  docker build -t check-orders:0.0.1 .
fi


list1_active=0
list2_active=0
list1=()
list2=()

for i in "$@"
do
	if [ "$i" == "--check" ]; then
		list1_active=1
	 	list2_active=0
	fi

	if [ "$i" == "--new_order" ]; then
	 	list1_active=0
	 	list2_active=1
	fi

	if [ "$i" != "--check" ] && [ $list1_active == 1 ]; then
		list1+=" $i"
	fi 

	if [ "$i" != "--new_order" ]  && [ $list2_active == 1 ]; then
		list2+=" $i"
	fi 

done


echo "*************"
echo $list1
echo "*************"
echo $list2

#TODO fix this call
#docker run -it --rm --name check_orders_container check_orders --check  $list1 --new_order $list2


#How to call
#./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 soda regular"
docker run -it --rm --name check_orders_container check_orders --check "$2" "$3"  --new_order "$5"
