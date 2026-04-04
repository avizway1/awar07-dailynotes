package main

import (
	"fmt"
	"net/http"
	"os"
	"time"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		hostname, _ := os.Hostname()
		fmt.Fprintf(w, `
<!DOCTYPE html>
<html>
<head><title>Aviz Academy - Docker Demo</title>
<style>
  body { font-family: sans-serif; background: #1A1A2E; color: #fff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
  .card { background: #16213E; padding: 40px; border-radius: 12px; border-left: 5px solid #FF6600; text-align: center; }
  h1 { color: #FF6600; } span { color: #aaa; font-size: 14px; }
</style>
</head>
<body>
  <div class="card">
    <h1>🐳 Aviz Academy</h1>
    <h2>Docker Multi-Stage Build Demo</h2>
    <p>Container ID: <b>%s</b></p>
    <p>Time: <b>%s</b></p>
    <span>Built with Go · Served from a scratch container</span>
  </div>
</body>
</html>
`, hostname, time.Now().Format("2006-01-02 15:04:05"))
	})

	fmt.Println("Server running on :8080")
	http.ListenAndServe(":8080", nil)
}