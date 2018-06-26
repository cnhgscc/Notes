package main

import (
	"example/test"
	"fmt"
	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Printf("Hello, world.  Sqrt(2) = %v\n", test.Sqrt(2))
	fmt.Printf(AddPersonApi)

	app := gin.Default()

	app.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	app.Run() // listen and serve on 0.0.0.0:8080
}
