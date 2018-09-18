FROM golang:latest 
RUN mkdir /app 
ADD . /app/ 

WORKDIR /app 

RUN go get -u github.com/gin-gonic/gin
RUN go get -u github.com/gin-gonic/contrib/static
RUN go get -u github.com/gin-contrib/cors
RUN go build -o main .
 
CMD ["/app/main"]
