package main

import
(
	"time"
	"fmt"
	"os"
	"log"
        "github.com/influxdata/influxdb/client/v2"
	"github.com/shirou/gopsutil/mem"
	"github.com/shirou/gopsutil/host"
)

func openClient(username string, password string, influxAddress string) (client.Client, error) {
        fmt.Println("Importing data points.")
        c, err := client.NewHTTPClient(client.HTTPConfig{
                Addr:     influxAddress,
                Username: username,
                Password: password,
        })

	return c, err
}

func buildDataPoints() client.BatchPoints {
        batchPoints, _ := client.NewBatchPoints(client.BatchPointsConfig{
                Database:  "botnet",
                Precision: "s",
        })
	h, _ := host.Info()

	v, _ := mem.VirtualMemory()
	fmt.Printf("Total: %v, Free:%v, UsedPercent:%f%%\n", v.Total, v.Free, v.UsedPercent)
	tags := map[string]string{
		"hostname": h.Hostname,
	}
	fields := map[string]interface{}{
		"virtual_memory_total": v.Total,
		"virtual_memory_free": v.Free,
		"virtual_memory_used": v.UsedPercent,
	}

	pt, _ := client.NewPoint("utilization", tags, fields, time.Now())
	batchPoints.AddPoint(pt)
	return batchPoints
}

func main() {
	fmt.Println("Collecting status")
	username := os.Getenv("username")
	password := os.Getenv("password")
	addr := os.Getenv("address")
	fmt.Println(username,password,addr)
	client, err := openClient(username, password, addr)
        if err != nil {
                log.Fatalln("Error: ", err)
                return
        }

	batchPoints := buildDataPoints()

        err = client.Write(batchPoints)
        if err != nil {
                log.Fatalln(err)
        }
}
