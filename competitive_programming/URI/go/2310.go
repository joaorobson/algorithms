package main
import(
  "fmt"
)

func main(){
  var a int
  var sq1, sq2, bl1, bl2, at1,at2 float32 = 0,0,0,0,0,0;
  fmt.Scan(&a)
  for b:=0;b < a;b++{
    var s string;
    var a2,a3,a4,a5,a6,a7 float32;
    fmt.Scan(&s)
    fmt.Scan(&a2)
    fmt.Scan(&a3)
    fmt.Scan(&a4)
    fmt.Scan(&a5)
    fmt.Scan(&a6)
    fmt.Scan(&a7)
    sq1 += a2
    sq2 += a5
    bl1 += a3
    bl2 += a6
    at1 += a4
    at2 += a7
  }
  fmt.Println("Pontos de Saque:", fmt.Sprintf("%.2f",100*(sq2/sq1)), "%.")
  fmt.Println("Pontos de Bloqueio:", fmt.Sprintf("%.2f",100*(bl2/bl1)), "%.")
  fmt.Println("Pontos de Ataque:", fmt.Sprintf("%.2f",100*(at2/at1)), "%.")


}
