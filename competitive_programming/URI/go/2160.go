package main

import (
"fmt"
"bufio"
"os"
"strings"
)

func main() {
    //reading an integer
     reader := bufio.NewReader(os.Stdin)
      text, _ := reader.ReadString('\n')
      text = strings.TrimSuffix(text, "\n")

      if len(text) > 80{
        fmt.Println("NO")
      } else{
        fmt.Println("YES")
      }


}
