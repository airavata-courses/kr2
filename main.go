package main

import (
  "net/http"

  //"github.com/gin-gonic/contrib/static"
  "github.com/gin-gonic/gin"
  "github.com/gin-contrib/cors"
)

func main() {
  // Set the router as the default one shipped with Gin
  router := gin.Default()

  // Serve frontend static files
  // router.Use(static.Serve("/", static.LocalFile("./views", true)))

  //router.Use(cors.Default())
  config := cors.DefaultConfig()
  config.AllowAllOrigins = true
  router.Use(cors.New(config))

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
