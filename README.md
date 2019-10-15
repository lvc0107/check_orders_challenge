# check_orders_challenge

**How to use**

1. clone this repo:


2. build docker image:
 
 ```docker build -t check-orders:0.0.1 .```
 
3. Execute some test 

Run:

```
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 soda regular"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 sodas regular"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "2 sodas regular"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "3 sodas regular"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "3 sodas regular"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "3 sugar free sodas"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 drink regular"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 drinks regular"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 regular soda"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 regular sodas"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 regular drink"
./run.sh  --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 regular drinks"
```
# TODO complete:

I have an error when I passing array of string with white space from
run.sh to the app.py
The shell script parse each token omiting ""
 
check: ['2', 'large', 'pepperoni', 'pizzas', '3', 'sugar', 'free', 'sodas']
new_order: ['1', 'soda', 'regular']

So in order to test custom array os string the following commands should be used:

```
docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 soda regular"

docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 sodas regular"

docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "2 sodas regular"

docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "3 sodas regular"

docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "3 sugar free sodas"

docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 drink regular"

docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 drinks regular"
 
docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 regular soda"

docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 regular sodas"
   
docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 regular drink"

docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 regular drinks"

docker run -it --rm --name check_orders_container check_orders --check "2 large pepperoni pizzas" "3 sugar free sodas" --new_order "1 regular drinks", "1 large pepperoni pizzas"
```# check_orders_challenge
