defmodule Aoc2015 do
  def day_1() do
    contents = File.read!("input.txt")

    total = Enum.reduce(String.to_charlist(contents), 0, fn ch, acc -> 
      acc + case List.to_string([ch]) do
        "(" -> 1
        ")" -> -1
        _   -> 0
      end
    end)

    total
  end
end

IO.puts(Aoc2015.day_1())