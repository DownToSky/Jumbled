-- problem 1
myLast :: [a] -> a 
myLast([x]) = x
myLast(x:xs) = myLast(xs) 

-- problem 2
myButLast :: [a] -> a
myButLast([x,y]) = x
myButLast(x:xs) = myButLast(xs)

-- problem 3
elementAt :: [a] -> (Int -> a)
elementAt [] i = error "Bad Index"
elementAt (x:xs) 1 = x
elementAt (x:xs) i = elementAt xs (i-1)

-- problem 4
myLength :: [a] ->

-- Problem Quicksort
quicksort :: [Int] -> [Int]
quicksort [] = []
quicksort [x] = [x]
quicksort x:xs = (quicksort $ filter (<x) xs) ++ [x] ++ (quicksort $ filter (>=x) xs)

