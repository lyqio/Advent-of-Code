require 'set'

$seen = Set[]

def count(lns, i, q)
  if lns[i][q] == '9' && !$seen.include?([i, q]) then
    $seen << [i, q]
    return 1
  end

  down = lns[i+1][q] rescue nil
  up = if i-1 < 0 then nil else lns[i-1][q] end
  left = if q-1 < 0 then nil else lns[i][q-1] end 
  right = lns[i][q+1] rescue nil

  moves = []
  if down != nil && down.to_i-lns[i][q].to_i == 1 then
    moves << [i+1, q]  
  end

  if up != nil && up.to_i-lns[i][q].to_i == 1 then
    moves << [i-1, q]
  end

  if left != nil && left.to_i-lns[i][q].to_i == 1 then
    moves << [i, q-1]
  end

  if right != nil && right.to_i-lns[i][q].to_i == 1 then
    moves << [i, q+1]
  end

  if moves.length == 0 then
    return 0
  end

  total = 0
  for move in moves do
    total += count(lns, move[0], move[1])
  end

  total
end

def part_1(lns)
  total = 0
  for i in (0..lns.length-1) do 
    for q in (0..lns[0].length-1) do
      if lns[i][q] == '0' then
        total += count(lns, i, q) 
        $seen.clear
      end
    end
  end

  total
end

def reaches_9(lns, i, q)
  if lns[i][q] == '9' then
    return true
  end

  down = lns[i+1][q] rescue nil
  up = if i-1 < 0 then nil else lns[i-1][q] end
  left = if q-1 < 0 then nil else lns[i][q-1] end 
  right = lns[i][q+1] rescue nil

  moves = []
  if down != nil && down.to_i-lns[i][q].to_i == 1 then
    moves << [i+1, q]  
  end

  if up != nil && up.to_i-lns[i][q].to_i == 1 then
    moves << [i-1, q]
  end

  if left != nil && left.to_i-lns[i][q].to_i == 1 then
    moves << [i, q-1]
  end

  if right != nil && right.to_i-lns[i][q].to_i == 1 then
    moves << [i, q+1]
  end

  if moves.length == 0 then
    return false
  end

  for move in moves do
    if reaches_9(lns, move[0], move[1]) then
      return true
    end
  end

  return false
end

def count2(lns, i, q)
  if lns[i][q] == '9' then
    return 1
  end

  down = lns[i+1][q] rescue nil
  up = if i-1 < 0 then nil else lns[i-1][q] end
  left = if q-1 < 0 then nil else lns[i][q-1] end 
  right = lns[i][q+1] rescue nil

  moves = []
  if down != nil && down.to_i-lns[i][q].to_i == 1 then
    moves << [i+1, q]  
  end

  if up != nil && up.to_i-lns[i][q].to_i == 1 then
    moves << [i-1, q]
  end

  if left != nil && left.to_i-lns[i][q].to_i == 1 then
    moves << [i, q-1]
  end

  if right != nil && right.to_i-lns[i][q].to_i == 1 then
    moves << [i, q+1]
  end

  if moves.length == 0 then
    return 0
  end

  total = 0
  for move in moves do
    total += count2(lns, move[0], move[1]) 
  end

  total
end

def part_2(lns)
  total = 0
  for i in (0..lns.length-1) do
    for q in (0..lns.length-1) do
      if lns[i][q] == '0' then
        total += count2(lns, i, q) 
      end
    end
  end

  total
end

def main
  lns = File.read("input.txt").lines
  puts part_1 lns
  puts part_2 lns
end

main
