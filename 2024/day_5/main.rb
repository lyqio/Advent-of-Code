
def part_1(lns)
  i = 0
  rules = []
  for line in lns do
    if line.strip == "" then
      break
    end

    rules.push line.split('|').map{|x| Integer(x.strip)}
    i += 1
  end
  
  total = 0
  for q in (i+1..lns.length-1) do
    this_line = lns[q].split(',').map{|x| Integer(x.strip)}
    in_order = true

    for c in (0..this_line.length-1) do
      for j in (1..this_line.length-1) do
        if rules.include?([this_line[j], this_line[j-1]]) then
          in_order = false
        end
      end
    end
    
    midpoint = (this_line.length/2).floor
    total += this_line[midpoint] if in_order
  end

  total
end

def part_2(lns)
  i = 0
  rules = []
  for line in lns do
    if line.strip == "" then
      break
    end

    rules.push line.split('|').map{|x| Integer(x.strip)}
    i += 1
  end
  
  total = 0
  for q in (i+1..lns.length-1) do
    this_line = lns[q].split(',').map{|x| Integer(x.strip)}
    in_order =  true

    for c in (0..this_line.length-1) do
      for j in (1..this_line.length-1) do
        if rules.include?([this_line[j], this_line[j-1]]) then
          in_order = false
          temp = this_line[j]
          this_line[j] = this_line[j-1]
          this_line[j-1] = temp
        end
      end
    end
    
    midpoint = (this_line.length/2).floor
    total += this_line[midpoint] unless in_order 
  end

  total
end

def main
  lns = File.read("input.txt").lines
  puts part_1 lns
  puts part_2 lns
end

main
