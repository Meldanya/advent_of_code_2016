import Data.Char
import Data.List

import Input

type PosDir = (Int, Int, Int)
type Move = (Int, Int)

dist :: String -> Int
dist = read . filter isNumber

turn :: String -> Int
turn dir
    | "R" `isInfixOf` dir = 1
    | otherwise = -1

split :: String -> [String]
split = words . filter (/= ',')

recombine :: [String] -> [Move]
recombine inp = zip (map turn inp) (map dist inp)

-- Modulo as in Python.
mod_ :: Int -> Int -> Int
mod_ a n = ((a `mod` n) + n) `mod` n

next :: Int -> Int -> Int
next cur dir = (cur + dir) `mod_` 4

walk :: PosDir -> Move -> PosDir
walk (0, x, y) (dir, dist) = (next 0 dir, x + dir * dist,       y       )
walk (1, x, y) (dir, dist) = (next 1 dir,       x       , y - dir * dist)
walk (2, x, y) (dir, dist) = (next 2 dir, x - dir * dist,       y       )
walk (3, x, y) (dir, dist) = (next 3 dir,       x       , y + dir * dist)

taxi_dist :: PosDir -> Int
taxi_dist (_, x, y) = abs x + abs y

main = do
    let end = foldl walk (0, 0, 0) (recombine $ split input)
    let res = taxi_dist end
    print res
