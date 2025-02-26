package main

import (
	// "os"
	// "github.com/sashabaranov/go-openai"
	"github.com/gofiber/fiber/v2"
	// "github.com/gofiber/utils"
)

// var mistralClient *openai.Client

// func init() {
// 	apiKey := os.Getenv("MISTRAL_API_KEY")
// 	if apiKey == "" {
// 		log.Fatal("API_KEY missing")
// 	}
// 	mistralClient = openai.NewClient(apiKey)
// }

func handler(c *fiber.Ctx) error {
	var r string
	if c.Params("foo") == "foo" {
		r = "Hello World"
		// r = string(c.Params("foo"))
		return c.SendString(r)
	}
	return c.SendString(r)
}

func main() {
	app := fiber.New()
	app.Get("/:foo", handler)
	app.Listen(":8080")
}