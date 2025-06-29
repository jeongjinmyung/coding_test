package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	t, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < t; i++ {
		scanner.Scan()
		line := scanner.Text()
		parts := strings.Split(line, " ")

		nums := make([]float64, 6)

		for i, val := range parts {
			f, err := strconv.ParseFloat(val, 64)
			if err != nil {
				panic(err)
			}
			nums[i] = f
		}
		result := getTargetNum(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])
		fmt.Println(result)
	}

}

func getTargetNum(x1, y1, r1, x2, y2, r2 float64) int {
	dx := x2 - x1
	dy := y2 - y1
	distance := math.Hypot(dx, dy)

	if distance == 0 {
		if r1 == r2 {
			return -1
		}
		return 0
	} else if distance > r1+r2 {
		return 0
	} else if distance == r1+r2 {
		return 1
	} else if math.Abs(r1-r2) < distance && distance < r1+r2 {
		return 2
	} else if distance == math.Abs(r1-r2) {
		return 1
	} else {
		return 0
	}
}