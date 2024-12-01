
class Day1
  def Day1.pt1(lns)
    left = []
    right = []
    for line in lns do
      left.push(Integer(line.split("   ")[0]))
      right.push(Integer(line.split("   ")[1]))
    end
    
    left.sort!
    right.sort!

    total = 0
    for i in (0..right.length-1) do
      total += (right[i]-left[i]).abs 
    end

    total
  end

  def Day1.pt2(lns)
    left = []
    right = []
    for line in lns
      left.push(Integer(line.split("   ")[0]))
      right.push(Integer(line.split("   ")[1]))
    end
    
    left.sort!
    right.sort!

    total = 0
    for i in (0..right.length-1) do
      total += left[i]*right.count(left[i]) 
    end

    total
  end
end

def main() 
  lns = File.read("input.txt").lines
  puts Day1.pt1 lns
  puts Day1.pt2 lns
end

main
