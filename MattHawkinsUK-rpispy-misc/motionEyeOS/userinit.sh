location="Garden"
user="replace_me_with_your_user_key"
token="replace_me_with_your_api_token"

sleep 10

port="40000"
ip=$(curl -s https://api.ipify.org)
ip="$ip:$port"

python /data/pushover.py $location $ip $user $token > /var/log/pushover &