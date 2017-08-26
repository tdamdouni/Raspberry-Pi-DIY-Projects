FROM golang:1.7

ADD ./app.go ./app.go
RUN go get github.com/shirou/gopsutil && \
 go get github.com/influxdata/influxdb/client/v2


CMD ["go", "run", "app.go"]
