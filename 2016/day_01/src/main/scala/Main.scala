
def part_1 = 
  val directions = Array((-1, 0), (0, 1), (1, 0), (0, -1))
  val lines = scala.io.Source.fromFile("src/main/scala/input.txt").mkString.split(", ")

  var current_dir = 0
  var current_location = (0, 0)
  for i <- lines
  do
    if i.charAt(0) == 'R' then
      current_dir = (current_dir+1)%4
    else
      current_dir = (current_dir-1)%4
      if current_dir < 0 then
        current_dir = 4+current_dir

    val dist_to_move = (i.substring(1)).toInt
    current_location = (current_location(0) + (dist_to_move*directions(current_dir)(0)), current_location(1)+(dist_to_move*directions(current_dir)(1)))
  
  println(current_location(0).abs + current_location(1).abs)
     

@main def main() =
  part_1
