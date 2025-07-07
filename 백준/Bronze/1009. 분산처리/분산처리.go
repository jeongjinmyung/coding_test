package main

import (
	"bufio"
	"fmt"
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
		nums := strings.Fields(line)

		a, _ := strconv.Atoi(nums[0])
		b, _ := strconv.Atoi(nums[1])

		result := solution(a, b)
		fmt.Println(result)
	}

}

func solution(a int, b int) int {
	a = a % 10

	cycles := map[int][]int{
		0: {10},
		1: {1},
		2: {2, 4, 8, 6},
		3: {3, 9, 7, 1},
		4: {4, 6},
		5: {5},
		6: {6},
		7: {7, 9, 3, 1},
		8: {8, 4, 2, 6},
		9: {9, 1},
	}
	cycle := cycles[a]
	cycleLen := len(cycle)

	idx := (b - 1) % cycleLen
	return cycle[idx]
}
