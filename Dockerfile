FROM golang:latest 
RUN mkdir /app 
ADD . /app/ 

WORKDIR /app 

RUN go get -u github.com/gin-gonic/gin
RUN go get -u github.com/gin-gonic/contrib/static
RUN go build -o main .
 
CMD ["/app/main"]
