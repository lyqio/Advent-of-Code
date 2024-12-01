
class Day1
  def Day1.pt1
    left = []
    right = []
    Integer(gets).times {
      line = gets
      left.push(Integer(line.split("   ")[0]))
      right.push(Integer(line.split("   ")[1]))
    }
    
    left.sort!
    right.sort!

    total = 0
    for i in (0..right.length-1) do
      total += (right[i]-left[i]).abs 
    end

    total
  end

  def Day1.pt2
    left = []
    right = []
    Integer(gets).times {
      line = gets
      left.push(Integer(line.split("   ")[0]))
      right.push(Integer(line.split("   ")[1]))
    }
    
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
  file = File.new("input.txt", "r")
  data = file.read
  file.close

  puts data
  puts Day1.pt1
end

main
