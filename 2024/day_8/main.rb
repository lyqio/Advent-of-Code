require 'set'

def part_1(lns)
  antennas = {}
  unique_chars = Set[]
  node_positions = Set[] 

  for i in (0..lns.length-1) do
    for q in (0..lns.length-1) do
      if lns[i][q] != '.' then
        unique_chars += [lns[i][q]]
        antennas[lns[i][q]] = []
      end
    end
  end

  for i in (0..lns.length-1) do
    for q in (0..lns.length-1) do
      if lns[i][q] != '.' then
        antennas[lns[i][q]] += [[i, q]]
      end
    end
  end

  for unique in unique_chars do
    coords = antennas[unique]
    for i in (0..coords.length) do
      for q in (i+1..coords.length) do
        point_1 = coords[i]
        point_2 = coords[q]

        if point_2 == nil then
          break
        end

        diff_x = point_1[0] - point_2[0]
        diff_y = point_1[1] - point_2[1]
        
        node_positions += [[point_1[0]+diff_x, point_1[1]+diff_y]]
        node_positions += [[point_2[0]-diff_x, point_2[1]-diff_y]]
      end
    end
  end

  for pos in node_positions do
    if (lns[pos[0]][pos[1]] rescue nil) == nil then
      next
    end

    lns[pos[0]][pos[1]] = '#'
  end

  cnt = 0
  for node in node_positions do
    unless node[0] < 0 || node[0] >= lns.length || node[1] < 0 || node[1] >= lns.length then
      cnt += 1
    end
  end

  cnt
end

def part_2(lns)
  antennas = {}
  unique_chars = Set[]
  node_positions = Set[] 

  for i in (0..lns.length-1) do
    for q in (0..lns.length-1) do
      if lns[i][q] != '.' then
        node_positions += [[i, q]]
        unique_chars += [lns[i][q]]
        antennas[lns[i][q]] = []
      end
    end
  end

  for i in (0..lns.length-1) do
    for q in (0..lns.length-1) do
      if lns[i][q] != '.' then
        antennas[lns[i][q]] += [[i, q]]
      end
    end
  end

  for unique in unique_chars do
    coords = antennas[unique]
    for i in (0..coords.length) do
      for q in (i+1..coords.length) do
        point_1 = coords[i]
        point_2 = coords[q]

        if point_2 == nil || point_1 == nil then
          break
        end

        diff_x = point_1[0] - point_2[0]
        diff_y = point_1[1] - point_2[1]
       
        j = 1
        new_point_1 = [point_1[0]+(diff_x*j), point_1[1]+(diff_y*j)]
        while new_point_1[0] >= 0 && new_point_1[0] <= lns.length && new_point_1[1] >= 0 && new_point_1[1] <= lns.length do
          node_positions += [new_point_1]
          new_point_1 = [point_1[0]+(diff_x*j), point_1[1]+(diff_y*j)]
          j += 1
        end

        j = 1
        new_point_2 = [point_2[0]-(diff_x*j), point_2[1]-(diff_y*j)]
        while new_point_2[0] >= 0 && new_point_2[0] <= lns.length && new_point_2[1] >= 0 && new_point_2[1] <= lns.length do
          node_positions += [new_point_2]
          new_point_2 = [point_2[0]-(diff_x*j), point_2[1]-(diff_y*j)]
          j += 1
        end
      end
    end
  end

  cnt = 0
  for node in node_positions do
    unless node[0] < 0 || node[0] >= lns.length || node[1] < 0 || node[1] >= lns.length then
      lns[node[0]][node[1]] = '#'
      cnt += 1
    end
  end

  cnt
end

def main
  lns = File.read("input.txt").lines
  puts part_2 lns
end

main
