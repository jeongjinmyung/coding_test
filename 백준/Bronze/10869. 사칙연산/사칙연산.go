package main

import "fmt"

func main() {
    var a, b int
    
    if _, err := fmt.Scanln(&a, &b); err != nil {
        fmt.Println("Error", err)
        return
    }
    
    fmt.Println(a + b)
    fmt.Println(a - b)
    fmt.Println(a * b)
    
    if b == 0 {
        fmt.Println("division by zero")
        return
    }
    fmt.Println(a / b)
    fmt.Println(a % b)
}