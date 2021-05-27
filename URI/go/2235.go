package main

import (
"fmt"
)

func main() {

    //reading an integer
      var a = 0
      var b = 0
      var c = 0
      fmt.Scan(&a)
      fmt.Scan(&b)
      fmt.Scan(&c)

      if a - b == 0 || a - c == 0 || b - c == 0{
        fmt.Println("S")
      } else if a + b - c == 0 || a - b + c == 0 || a - b - c == 0 {
        fmt.Println("S")
      } else if -a + b + c == 0 || -a + b - c == 0 || -a - b + c == 0 {
        fmt.Println("S")
      } else{
        fmt.Println("N")
      }
}
