
def perm(t)
  perms = []
  for i in (0..t) do
    perms << i
  end

  perms
end

def calc(ax, ay, bx, by, targetx, targety)
  x_guess = 0
  y_guess = 0
  t = (targetx.to_f/[ax, bx].max.to_f).floor
  cur_i = 0
  cur_q = 0

  finish = false
  while x_guess != targetx and y_guess != targety
    per = perm(t)
    for i in (0..per.length-1) do
      for q in (0..per.length-1) do
        next if i == q

        cur_i = i
        cur_q = q
        x_guess = (ax*per[i]) + (bx*per[q])
        y_guess = (ay*per[i]) + (by*per[q])
        
        break if x_guess == targetx and y_guess == targety
      end
      break if x_guess == targetx and y_guess == targety

      if per[-1]*ax > targetx and per[-1]*bx > targetx then
        finish = true
        break
      end
    end

    break if finish
    t += 1
  end

  return [-1, -1] if finish
  [cur_i, cur_q]
end

def part_1(lns)

  p calc(26, 66, 67, 21, 12748, 12176)

  # total = 0
  # for i in (2..lns.length-1).step(4) do
  #   button_a = lns[i-2].scan(/\d+/)
  #   button_b = lns[i-1].scan(/\d+/)
  #   prize = lns[i].scan(/\d+/)

  #   p button_a, button_b, prize

  #   presses = calc(button_a[0].to_i, button_a[1].to_i, button_b[0].to_i, button_b[1].to_i, prize[0].to_i, prize[1].to_i)
  #   total += (presses[0]*3) + (presses[1])
  # end

  total
end

def part_2(lns)
  0
end

def main
  lns = File.read("sample.txt").lines
  puts part_1 lns
  puts part_2 lns
end

main
