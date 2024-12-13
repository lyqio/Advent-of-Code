require 'set'

$visited = Set[]

def bfs(lns, i, q)
  region = lns[i][q] rescue nil
  return if region == nil

  $visited << [i, q]

  moves = []
  if q > 0 and !$visited.include?([i, q-1]) and lns[i][q-1] == region then
    moves << [i, q-1]
  end

  if i > 1 and !$visited.include?([i-1, q]) and lns[i-1][q] == region then
    moves << [i-1, q]
  end

  if q < lns[0].length-1 and !$visited.include?([i, q+1]) and lns[i][q+1] == region then
    moves << [i, q+1]
  end

  if i < lns.length-1 and !$visited.include?([i+1, q]) and lns[i+1][q] == region then
    moves << [i+1, q]
  end

  if moves.length == 0 then
    return 
  end

  for move in moves do
    bfs(lns, move[0], move[1])
  end
end

$perim_visit = Set[]
$counted = Set[]

def perimeter(lns, i, q)
  region = lns[i][q] rescue nil
  return 0 if region == nil
  $perim_visit << [i, q]

  perim = 0
  moves = []
  unless $perim_visit.include?([i, q-1]) then
    if q < 1 or lns[i][q-1] != region then
      $counted << [i, q-1]
      perim += 1
    else
      moves << [i, q-1]
    end
  end

  unless $perim_visit.include?([i-1, q]) then
    if i < 1 or lns[i-1][q] != region then
      $counted << [i-1, q]
      perim += 1
    else
      moves << [i-1, q]
    end
  end

  unless $perim_visit.include?([i, q+1]) then
    if q+1 >= lns[0].length or lns[i][q+1] != region then
      $counted << [i, q+1]
      perim += 1
    else
      moves << [i, q+1]
    end
  end

  unless $perim_visit.include?([i+1, q]) then
    if i+1 >= lns.length or lns[i+1][q] != region then
      $counted << [i+1, q]
      perim += 1
    else
      moves << [i+1, q]
    end
  end

  if moves.length == 0 then
    return perim
  end

  for move in moves do
    perim += perimeter(lns, move[0], move[1])
  end

  perim
end

def part_1(lns)
  total = 0

  last_len = 0
  for i in (0..lns.length) do
    for q in (0..lns[0].length) do
      unless $visited.include?([i, q]) then
        area = bfs(lns, i, q) 
        total_a = $visited.length-last_len
        last_len = $visited.length

        perim = perimeter(lns, i, q)
        total_p = $counted.length
        $perim_visit.clear
        $counted.clear

        p "area = #{total_a} | perimeter = #{total_p}"

        total += (total_a*total_p)
      end
    end
  end

  total
end

def part_2(lns)
  0
end

def main
  lns = File.read("sample.txt").lines.map{ |x| x.strip }
  puts part_1 lns
  puts part_2 lns
end

main
