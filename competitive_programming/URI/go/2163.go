package main

import (
"fmt"
)

func main() {

    //reading an integer
      var a1 = 0
      var a2 = 0
      fmt.Scan(&a1)
      fmt.Scan(&a2)
      m := make([][]int, 1000) //initialize the slice of slices
      for x := range m{
       m[x] = make([]int, 1000) // intialize every slice within the slice of slices
      }
      r1 := 0
      r2 := 0 
      j := 1
      for s:=0; s < a1; s++ {
        for e:=0;e < a2; e++{
          fmt.Scanf("%d",&m[s][e])
        }
      }
      for i:=1; i < len(m[i]) - 1; i++ {
        if r1 > 0 {
          break
        }
        for j < len(m[i]) - 1{
          if m[i][j] == 42{
            if m[i-1][j-1] == 7 && m[i-1][j] == 7 && m[i-1][j+1] == 7{
              if m[i][j-1] == 7 && m[i][j+1] == 7{
                if m[i+1][j-1] == 7 && m[i+1][j] == 7 && m [i+1][j+1] == 7 {
                  r1 = i
                  break
                }
              }
            }
          }
          j++
        }
      }
      if r1 == 0 && r2 == 0{

      fmt.Println(0, 0)
      }else{
      fmt.Println(r1 + 1, j + 1)
    }


}

