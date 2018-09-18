package main

import (
  "net/http"

  "github.com/gin-gonic/contrib/static"
  "github.com/gin-gonic/gin"
)

func main() {
  // Set the router as the default one shipped with Gin
  router := gin.Default()

  // Serve frontend static files
  router.Use(static.Serve("/", static.LocalFile("./views", true)))

  // Setup route group for the API
  Goapi := router.Group("/api")
  {
    Goapi.GET("/", func(cont *gin.Context) {
      cont.JSON(http.StatusOK, gin.H {
        "result": "API for US Naukri system",
      })
    })
  }

  jobrec := router.Group("/jobrec")
  {
    jobrec.GET("/", func(c *gin.Context) {
      c.JSON(http.StatusOK, gin.H {
        "message": "Recommendation for your job profile underway",
      })
    })
  }

  


  // Start and run the server
  router.Run(":3050")
}
