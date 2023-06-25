package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func AddPersonApi(c *gin.Context) {
	c.String(http.StatusOK, "It works")
}
