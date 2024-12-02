
def part_1(lns)
  cnt = 0
  for line in lns do
    levels = line.split(' ').map{ |x| Integer(x)}
    unless levels == levels.sort || levels == levels.sort.reverse then
      next
    end

    condition_2 = true
    for i in (1..levels.length-1) do
      if (levels[i]-levels[i-1]).abs < 1 || (levels[i]-levels[i-1]).abs > 3 then
        condition_2 = false
        break
      end
    end

    if condition_2 == false then
      next
    end
  
    cnt += 1
  end

  cnt
end

def works(levels)
    unless levels == levels.sort || levels == levels.sort.reverse then
      return false
    end

    condition_2 = true
    for i in (1..levels.length-1) do
      if (levels[i]-levels[i-1]).abs < 1 || (levels[i]-levels[i-1]).abs > 3 then
        condition_2 = false
        break
      end
    end

    condition_2
end

def part_2(lns)
  cnt = 0
  for line in lns do
    levels = line.split(' ').map{ |x| Integer(x)}

    if works(levels) then
      cnt += 1
    else
      for i in (0..levels.length-1) do
        a = levels.dup
        a.delete_at(i)

        if works(a) then
          cnt += 1
          break
        end
      end
    end
  end

  cnt
end

def main
  lns = File.read("input.txt").lines
  puts part_1 lns
  puts part_2 lns
end

main