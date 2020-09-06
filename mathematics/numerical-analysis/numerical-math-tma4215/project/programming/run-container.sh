docker build -t notebook . --file="Dockerfile-src"
docker run -p 8888:8888\
   -v $(pwd)/:/root/src \
   notebook

