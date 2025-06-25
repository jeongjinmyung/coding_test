package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scanln(&n)

	for i := 1; i <= n; i++ {
		stars := strings.Repeat("*", i)
		fmt.Println(stars)
	}
}