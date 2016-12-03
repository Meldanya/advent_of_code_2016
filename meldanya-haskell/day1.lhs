> import Data.Char
> import Data.List
> import Input

First we define some types that are useful later. The PosDir type represents a
direction we're facing and a position. The Move type represents a move, i.e. a
turn and a distance. A turn to the left is represented by -1 and a turn to the
right is represented by 1.

> type PosDir = (Int, Int, Int)
> type Move = (Int, Int)

Split takes a string as formatted in the input (e.g. "R1, L2, R2") and splits it
into a list of each move instruction.

> split :: String -> [String]
> split = words . filter (/= ',')

Dist reads out the distance from a move instruction string, e.g. dist "R3" -> 3.

> dist :: String -> Int
> dist = read . filter isNumber

Turn converts a turn from a string (e.g. "R") to an int as expected in the move
type.

> turn :: String -> Int
> turn dir
>     | "R" `isInfixOf` dir = 1
>     | otherwise = -1

Recombine takes a list of move instructions as strings and converts it into a
list of instructions of the Move type.

> recombine :: [String] -> [Move]
> recombine inp = zip (map turn inp) (map dist inp)

Since Haskell's modulo function doesn't handle negative numbers as is apropriate
for this use case, we define our own modulo function.

> mod_ :: Int -> Int -> Int
> mod_ a n = ((a `mod` n) + n) `mod` n

The next function returns the next direction to face given the current direction
and a turn (as an int).

> next :: Int -> Int -> Int
> next cur dir = (cur + dir) `mod_` 4

Walk returns the next position and orientation given the current one and a move
instruction.

> walk :: PosDir -> Move -> PosDir
> walk (0, x, y) (dir, dist) = (next 0 dir, x + dir * dist,       y       )
> walk (1, x, y) (dir, dist) = (next 1 dir,       x       , y - dir * dist)
> walk (2, x, y) (dir, dist) = (next 2 dir, x - dir * dist,       y       )
> walk (3, x, y) (dir, dist) = (next 3 dir,       x       , y + dir * dist)

Taxi distance computes the distance from the start to an arbitrary position.

> taxi_dist :: PosDir -> Int
> taxi_dist (_, x, y) = abs x + abs y

Main simply combines the previously defined functions and folds over the input
with the walk function. It then computes the taxi distance for the end point.

> main = do
>     let end = foldl walk (0, 0, 0) (recombine $ split input)
>     let res = taxi_dist end
>     print res
