require 'set'

def switch_direction(direction)
  if direction == [-1, 0] then
    direction = [0, 1]
  elsif direction == [0, 1] then
    direction = [1, 0]
  elsif direction == [1, 0] then
    direction = [0, -1]
  else
    direction = [-1, 0]
  end
  direction
end

def part_1(lns)
  direction = [-1, 0]
  position = []
  for i in (0..lns.length-1) do
    for q in (0..lns[i].length-1) do
      if lns[i][q] == '^' then
        position = [i, q]
      end
    end
  end

  has_moved = false
  turning_points = Set[] # for part 2
  known_coords = Set[]
  until position[0] < 0 || position[0] >= lns.length || position[1] < 0 || position[1] >= lns[0].length do
    unless lns[position[0]][position[1]] == '#' then
      has_moved = true
      known_coords.add([position[0], position[1]])
      position[0] += direction[0]
      position[1] += direction[1]
    else
      if turning_points.include?([position[0], position[1], direction]) && has_moved then
        return -1
      end

      has_moved = false
      turning_points.add([position[0], position[1], direction])
      position[0] -= direction[0]
      position[1] -= direction[1]
      direction = switch_direction direction
    end
  end

  known_coords.length
end

def part_2(lns)
  cnt = 0
  for i in (0..lns.length-1) do
    for q in (0..lns.length-1) do
      if lns[i][q] == '.' then
        lns[i][q] = '#'
        cnt += 1 if part_1(lns) == -1
        lns[i][q] = '.'
      end
    end
    puts "row #{i+1} of #{lns.length}"
  end

  cnt
end

def main
  lns = File.read("input.txt").lines.map{|x| x.strip}
  puts part_1 lns
  puts part_2 lns
end

main
