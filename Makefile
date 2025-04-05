lint:
		pylint --disable=C,R,W0621,W1508 src/*.py
install:
		pip install --upgrade pip && \
		pip install -r src/requirements.txt
