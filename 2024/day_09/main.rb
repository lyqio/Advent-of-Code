
def part_1(line)
  digits = []
  for i in (0..line.length-1) do
    if i % 2 == 0 then
      for q in (1..line[i].to_i) do
        digits << "#{i/2}"
      end
    else
      for q in (1..line[i].to_i) do
        digits << '.' 
      end
    end
  end

  ptr_end = digits.length-1
  ptr_start = 0
  while ptr_start <= ptr_end && ptr_start < digits.length do
    if digits[ptr_start] == '.' && digits[ptr_end] != '.' then
      digits[ptr_start] = digits[ptr_end]
      digits[ptr_end] = '.'
      ptr_start += 1
      ptr_end -= 1
    elsif digits[ptr_start] == '.' && digits[ptr_end] == '.' then
      while ptr_end > 0 && digits[ptr_end] == '.' do
        ptr_end -= 1
      end

      digits[ptr_start] = digits[ptr_end]
      digits[ptr_end] = '.'
      ptr_start += 1
      ptr_end -= 1
    elsif digits[ptr_start] != '.' && digits[ptr_end] != '.' then
      while ptr_start < digits.length && digits[ptr_start] != '.' do
        ptr_start += 1
      end

      digits[ptr_start] = digits[ptr_end]
      digits[ptr_end] = '.'
      ptr_start += 1
      ptr_end -= 1
    else
      while ptr_end > 0 && digits[ptr_end] == '.' do
        ptr_end -= 1
      end

      while ptr_start < digits.length && digits[ptr_start] != '.' do
        ptr_start += 1
      end

      digits[ptr_start] = digits[ptr_end]
      digits[ptr_end] = '.'
      ptr_start += 1
      ptr_end -= 1
    end
  end

  i = 0
  while i < digits.length && digits[i] != '.' do
    i += 1
  end

  i += 1
  if digits[i] != '.' then
    digits[i-1] = digits[i]
    digits[i] = '.'
  end

  total = 0
  for i in (0..digits.length-1) do
    next if digits[i] == '.'
    total += (i*digits[i].to_i)
  end

  total
end

def part_2(line)
  files = []
  space = []
  pos = 0
  for i in (0..line.length-1) do
    if i%2 == 0 then
      files << [i/2, pos, line[i].to_i] 
      pos += line[i].to_i
    else
      space << [-1, pos, line[i].to_i]
      pos += line[i].to_i
    end
  end

  for file in files.reverse do
    for sp in space do
      if sp[1] < file[1] and sp[2] >= file[2] then
        file[1] = sp[1]
        sp[1] += file[2]
        sp[2] = sp[2] - file[2]
      end
    end
  end

  total = 0
  for file in files do
    for i in (0..file[2]-1) do
      total += file[0]*(file[1]+i)
    end
  end

  total
end
# 2858

def main
  lns = File.read("input.txt").strip
  puts part_2 lns
end

main
