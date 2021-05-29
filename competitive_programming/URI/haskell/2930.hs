readNumbers :: String -> [Int]
readNumbers = map read . words

main = do
  input <- getLine
  case readNumbers input of
    [a,b] -> if a > b 
             then putStrLn "Eu odeio a professora!" 
             else if (a + 3) <= b then putStrLn "Muito bem! Apresenta antes do Natal!"
             else do
                  let c = b + 2
                  putStrLn "Parece o trabalho do meu filho!"
                  if c <= 24
                  then putStrLn "TCC Apresentado!"
                  else putStrLn "Fail! Entao eh nataaaaal!"
