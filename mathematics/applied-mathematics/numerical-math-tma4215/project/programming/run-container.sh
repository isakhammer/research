docker build -t notebook . --file="Dockerfile-src" --no-cache
docker run -p 8888:8888\
   -v $(pwd)/:/root/src \
   --rm \
   notebook

