

all: build run


build: docker-build-morfeusz docker-build-krnnt


docker-build-morfeusz:
	docker build -t nlp_workshop/morfeusz -f ./docker/morfeusz/Dockerfile .

docker-build-krnnt:
	docker build -t nlp_workshop/krnnt -f ./docker/krnnt/Dockerfile .


run:


docker-run-morfeusz:
	docker run -ti -p 8888:8888 -v $(shell pwd):/home/local nlp_workshop/morfeusz jupyter notebook --ip 0.0.0.0 --no-browser --allow-root

docker-run-krnnt:
	docker run -ti -p 8888:8888 -v $(shell pwd):/home/local nlp_workshop/krnnt jupyter notebook --ip 0.0.0.0 --no-browser
