
def dp(target, cur, line) 
  if line.length == 0 then
    if cur == target then
      return true
    end
    return false
  end

  value_1 = dp(target, cur+line[0], line[1..])
  value_2 = dp(target, cur*line[0], line[1..])

  value_1 || value_2
end

def dp_pt2(target, cur, line) 
  if line.length == 0 then
    if cur == target then
      return true
    end
    return false
  end

  value_1 = dp_pt2(target, cur+line[0], line[1..])
  value_2 = dp_pt2(target, cur*line[0], line[1..])
  value_3 = dp_pt2(target, Integer(cur.to_s+line[0].to_s), line[1..])

  value_1 || value_2 || value_3
end

def part_1(lns)
  cnt = 0
  for line in lns do
    value = line.split(": ")
    ans = Integer(value[0])

    nums = value[1].split(' ').map{ |x| Integer(x) }
    cnt += ans if dp(ans, nums[0], nums[1..])
  end

  cnt
end

def part_2(lns)
  cnt = 0
  for line in lns do
    value = line.split(": ")
    ans = Integer(value[0])

    nums = value[1].split(' ').map{ |x| Integer(x) }
    cnt += ans if dp_pt2(ans, nums[0], nums[1..])
  end

  cnt
end

def main
  lns = File.read("input.txt").lines
  puts part_1 lns
  puts part_2 lns
end

main
