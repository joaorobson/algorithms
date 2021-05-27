package main
import(
  "fmt"
  "sort"
)

func sum(input []float64) float64 {
    sum := 0.0

    for _, i := range input {
        sum += i
    }

    return sum
}
func main(){
  var a int
  fmt.Scan(&a)
  for b:=0;b < a;b++{
    n :=[]float64{}
    var s string;
    var a1,a2,a3,a4,a5,a6,a7,a8 float64;
    fmt.Scan(&s)
    fmt.Scan(&a1)
    fmt.Scan(&a2)
    n = append(n,a2)
    fmt.Scan(&a3)
    n = append(n,a3)
    fmt.Scan(&a4)
    n = append(n,a4)
    fmt.Scan(&a5)
    n = append(n,a5)
    fmt.Scan(&a6)
    n = append(n,a6)
    fmt.Scan(&a7)
    n = append(n,a7)
    fmt.Scan(&a8)
    n = append(n,a8)
    sort.Float64s(n)
    fmt.Println(s, fmt.Sprintf("%.2f",a1*sum(n[1:6])))
  }


}
