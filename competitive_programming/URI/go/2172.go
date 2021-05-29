package main

import (
"fmt"
)

func main() {
  var a uint64
  var b uint64
  fmt.Scan(&a)
  fmt.Scan(&b)
  for a != 0 {
  fmt.Println(a*b)
  fmt.Scan(&a)
  fmt.Scan(&b)
  }



}
