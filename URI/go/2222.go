package main

import (
"fmt"
)
func intersection(a []uint32, b[]uint32)int{
  res := make(map[uint32]uint32)
  if len(a) > len(b){
    for _, n := range a {
      for t,_ := range b{
        if b[t] == n {
          res[n] = 1
        }
      }
    }
  }else{
    for _, n := range b {
      for t,_ := range a{
        if a[t] == n {
          res[n] = 1
        }
      }
    }
  }
  return len(res)
}

func union(a []uint32, b[]uint32)int{
  res := make(map[uint32]uint32)
  for _, n := range a {
    res[n] = 1
	}
  for _, n := range b {
    res[n] = 1
  }
  return len(res)
}

func main() {

    //reading an integer
      var a = 0
      fmt.Scan(&a)
      i := 0
      for i < a {
        var b,c,d,f,g,h uint32
        var e,s,k,j uint32
        m := [][]uint32{}


        fmt.Scan(&b)
        k = 0
        for k < b {
          r := []uint32{}
          fmt.Scan(&c)
          j = 0
          for j < c{
            fmt.Scan(&d)
            r = append(r, d)
            j++
          }
          m = append(m, r)
          k++
        }
      fmt.Scan(&e)
      s = 0
      for s < e{
        fmt.Scan(&f)
        fmt.Scan(&g)
        fmt.Scan(&h)
        if f == 1{
          fmt.Println(intersection(m[g-1], m[h-1]))
        }else{
          fmt.Println(union(m[g-1], m[h-1]))
        }
        s++
      }
      i++
  }
}
