
def part_1(line)
  cnt = 0
  regex = /mul\(\d{1,3},\d{1,3}\)/
  a = line.scan regex

  for item in a do
    item.sub!("mul(", "")
    item.sub!(")", "") 

    values = item.split ','
    value1 = Integer(values[0])
    value2 = Integer(values[1])

    cnt += (value1*value2)
  end

  cnt
end

def part_2(line)
  cnt = 0
  regex = /do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)/
  on = 1
  a = line.scan regex

  for item in a do
    if item.match /do\(\)/ then
      on = 1
    elsif item.match /don't\(\)/ then
      on = 0
    else
      item.sub!("mul(", "")
      item.sub!(")", "") 

      values = item.split ','
      value1 = Integer(values[0])
      value2 = Integer(values[1])

      cnt += on*value1*value2
    end
  end

  cnt
end

def main
  lns = File.read("input.txt")
  puts part_1 lns
  puts part_2 lns
end

main
