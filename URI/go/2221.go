package main

import (
"fmt"
)

func main() {

    //reading an integer
      var a = 0
      fmt.Scan(&a)
      i := 0
      for i < a {
        var b,c,d,e,f,g,h, at1, at2 int
        fmt.Scan(&b)
        fmt.Scan(&c)
        fmt.Scan(&d)
        fmt.Scan(&e)
        fmt.Scan(&f)
        fmt.Scan(&g)
        fmt.Scan(&h)
        if e%2 == 0{
          at1 = (c + d)/2 + b
        } else{
          at1 = (c + d)/2
        }
        if h%2 == 0{
          at2 = (f + g)/2 + b
        } else{
          at2 = (f + g)/2
        }
        if at1 > at2{
          fmt.Println("Dabriel")
        } else if at1 < at2 {
          fmt.Println("Guarte")
        } else {
          fmt.Println("Empate")
        }

        i++
    }
}
