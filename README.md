# 2nd-order-attacks

1. Run the first flask app with sql injection: https://github.com/alex-nightvision/remediation-demo

	```
	git clone https://github.com/alex-nightvision/remediation-demo.git
	docker compose up -d --build
	```

2. Run this app and sql inject to make a request to the 1st app.

	```
	git clone https://github.com/alex-nightvision/remediation-demo.git
	pip install -r requirements.txt --break-system-packages
	python app.py
	./check-endpoint.sh
	```
