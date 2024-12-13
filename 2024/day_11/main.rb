
def part_1(line)
  stones = line.split(' ').map{ |x| Integer(x) }

  for i in (1..25) do
    for q in (0..stones.length-1) do
      if stones[q] == 0 then
        stones[q] = 1
      elsif stones[q].to_s.length%2 == 0 then
        half = stones[q].to_s.length/2
        u = stones[q].to_s[0..half-1]
        t = stones[q].to_s[half..stones[q].to_s.length-1]

        stones[q] = u.strip.to_i
        stones << t.strip.to_i
      else
        stones[q] *= 2024
      end
    end
  end

  stones.length
end

def part_2(line)
  stones = {}
  for i in line.split(' ') do
    stones[line[i].to_i] = 1
  end
  
  for i in (1..75) do
    #for stone in stones do
    #  for q in (1..stone[1]) do
    #    unless stone[1] == 0 then
    #      print stone[0], " "
    #    end
    #  end
    #end
    #puts ""

    for stone in stones.dup do
      next if stone[1] == 0

      if stone[0] == 0 then
        unless stones[1] == nil then
          stones[1] += stone[1]
        else
          stones[1] = stone[1]
        end

        stones[stone[0]] = 0
      elsif stone[0].to_s.length%2 == 0 then
        half = stone[0].to_s.length/2
        u = stone[0].to_s[0..half-1]
        t = stone[0].to_s[half..stone[0].to_s.length-1]

        unless stones[u.to_i] == nil then
          stones[u.to_i] += stone[1]
        else
          stones[u.to_i] = stone[1]
        end

        unless stones[t.to_i] == nil then
          stones[t.to_i] += stone[1]
        else
          stones[t.to_i] = stone[1]
        end

        stones[stone[0]] -= stone[1] 
      else
        unless stones[stone[0]*2024] == nil then
          stones[stone[0]*2024] += stone[1]
        else
          stones[stone[0]*2024] = stone[1]
        end

        stones[stone[0]] -= stone[1] 
      end
    end
  end

  cnt = 0
  for stone in stones do
    cnt += stone[1]
  end

  cnt
end

def main
  lns = File.read("input.txt").strip
  puts part_2 lns
end

main
