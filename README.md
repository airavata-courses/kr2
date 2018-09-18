#KR2

Asumming docker is already installed

steps to deploy locally

docker build -t jobRec .
docker run -p 3050:3050 -it jobRec
