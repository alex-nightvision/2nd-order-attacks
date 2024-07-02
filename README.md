# 2nd-order-attacks

1. Run the first remediation demo app locally: https://github.com/alex-nightvision/remediation-demo

	```
	git clone https://github.com/alex-nightvision/remediation-demo.git
	docker compose up -d --build
	```

2. Run this app and inject to make a request to the 1st app.

	```
	git clone https://github.com/alex-nightvision/remediation-demo.git
	pip install -r requirements.txt --break-system-packages
	python app.py
	```
3. Run the scan
	```
	# confirm its working
	./check-endpoint.sh

	# do a grep to show theres no s q l in the app
	./look-for-sql.sh

	# add target 
	nightvision app create -n 2nd-order-attack
	nightvision target create -n 2nd-order-attack -u http://127.0.0.1:5000 --type api
	nightvision swagger extract ./ -t 2nd-order-attack --lang python 

	# run
	nightvision scan -t 2nd-order-attack -a 2nd-order-attack
	```