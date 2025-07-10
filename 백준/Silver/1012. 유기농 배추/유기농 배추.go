package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	x, y int
}

var (
	dx       = []int{0, 0, -1, 1}
	dy       = []int{-1, 1, 0, 0}
	grid     [][]int
	visited  [][]bool
	M, N, K  int
)

func bfs(sx, sy int) {
	queue := []Point{{sx, sy}}
	visited[sx][sy] = true

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]

		for i := 0; i < 4; i++ {
			nx := curr.x + dx[i]
			ny := curr.y + dy[i]

			if nx >= 0 && nx < M && ny >= 0 && ny < N {
				if grid[nx][ny] == 1 && !visited[nx][ny] {
					visited[nx][ny] = true
					queue = append(queue, Point{nx, ny})
				}
			}
		}
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	tStr, _ := reader.ReadString('\n')
	T, _ := strconv.Atoi(strings.TrimSpace(tStr))

	for t := 0; t < T; t++ {
		line, _ := reader.ReadString('\n')
		parts := strings.Fields(line)
		M, _ = strconv.Atoi(parts[0])
		N, _ = strconv.Atoi(parts[1])
		K, _ = strconv.Atoi(parts[2])

		grid = make([][]int, M)
		visited = make([][]bool, M)
		for i := 0; i < M; i++ {
			grid[i] = make([]int, N)
			visited[i] = make([]bool, N)
		}

		for i := 0; i < K; i++ {
			posLine, _ := reader.ReadString('\n')
			posParts := strings.Fields(posLine)
			x, _ := strconv.Atoi(posParts[0])
			y, _ := strconv.Atoi(posParts[1])
			grid[x][y] = 1
		}

		count := 0
		for i := 0; i < M; i++ {
			for j := 0; j < N; j++ {
				if grid[i][j] == 1 && !visited[i][j] {
					bfs(i, j)
					count++
				}
			}
		}
		fmt.Println(count)
	}
}
