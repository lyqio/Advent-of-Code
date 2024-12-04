
def part_1(lns)
  cnt = 0
  for line in lns do
    cnt += line.scan("XMAS").length + line.scan("SAMX").length 
  end

  for i in (3..lns.length-1) do
    for q in (0..lns[0].length-1) do
      next if lns[i-3][q] == nil || lns[i][q] == nil
      value = lns[i][q] + lns[i-1][q] + lns[i-2][q] + lns[i-3][q]
    
      cnt += 1 if value == "XMAS" || value == "SAMX"
    end
  end

  for i in (3..lns.length-1) do
    for q in (3..lns.length-1) do
      value = lns[i][q] + lns[i-1][q-1] + lns[i-2][q-2] + lns[i-3][q-3]

      cnt += 1 if value == "XMAS" || value == "SAMX"
    end
  end
  
  for i in (3..lns.length-1) do 
    for q in (3..lns.length-1) do
      value = lns[i][q-3] + lns[i-1][q-2] + lns[i-2][q-1] + lns[i-3][q]
      cnt += 1 if value == "XMAS" || value == "SAMX"
    end
  end

  cnt
end

def is_mas?(str)
  str == "MAS" || str == "SAM"
end

def part_2(lns)
  cnt = 0
  for i in (2..lns.length-1) do
    for q in (2..lns.length-1) do
      a = lns[i][q] + lns[i-1][q-1] + lns[i-2][q-2]
      b = lns[i][q-2] + lns[i-1][q-1] + lns[i-2][q]

      if is_mas?(a) && is_mas?(b) then
        cnt += 1
        next
      end
      # puts "Scanning #{value1}, #{value2}, #{value3}, #{value4}" if (is_mas?(value1) && is_mas?(value2)) || (is_mas?(value3) && is_mas?(value4))
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
