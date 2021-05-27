main = do  
    a <- getLine  
    b <- getLine  
    if a > b
      then putStrLn (b ++ "\n" ++  a)
      else putStrLn (a ++ "\n" ++  b)
