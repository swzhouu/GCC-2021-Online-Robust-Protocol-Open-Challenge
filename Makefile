recv:
	python3 ./proposal/main.py receiver

send:
	python3 ./proposal/main.py sender

cmp:
	python3 ./proposal/cmp.py

send5:
	timeout 5 python3 ./proposal/main.py sender

recv/example:
	python3 ./example/main.py receiver

send/example:
	python3 ./example/main.py sender

cmp/example:
	python3 ./proposal/cmp.py

