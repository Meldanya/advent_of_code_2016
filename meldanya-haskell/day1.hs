import Data.Char
import Data.List

input = "R5, L5, R5, R3"

dist :: String -> Int
dist = read . filter isNumber

turn :: String -> Int
turn dir
    | "R" `isInfixOf` dir = 1
    | otherwise = -1

split = words . filter (/= ',')

combine inp = zip (map turn inp) (map dist inp)

{- walk (1, dist) pos = (dir + fst pos, -}

main = do
    let dirs = combine $ split input

    print dirs
