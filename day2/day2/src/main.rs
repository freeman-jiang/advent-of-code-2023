use std::{
    fs::File,
    io::{self, BufRead},
    path::Path,
    usize,
};

#[derive(Debug)]
struct Match {
    red: i64,
    blue: i64,
    green: i64,
}

const INITIAL: Match = Match {
    red: 12,
    blue: 14,
    green: 13,
};

fn main() {
    let f = File::open(Path::new("input.txt")).unwrap();

    let reader = io::BufReader::new(f);

    let mut part1 = 0;
    let mut part2 = 0;

    for (i, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        if parse_part1(&line) {
            part1 += i + 1;
        }

        part2 += parse_part2(&line);
    }

    dbg!(part1);
    dbg!(part2);
}

fn parse_part1(line: &str) -> bool {
    let games = line.split(":").collect::<Vec<_>>();
    let game = games[1].trim();
    let matches: Vec<_> = game.split(";").collect();

    for m in matches {
        let trimmed_m = m.trim();
        let reveals: Vec<_> = trimmed_m.split(",").collect();
        for r in reveals {
            let mut parts = r.trim().split(" ");
            let (num, color) = (
                parts.next().unwrap().parse::<usize>().unwrap(),
                parts.next().unwrap(),
            );

            let mut bag = INITIAL;

            match color {
                "red" => {
                    bag.red -= num as i64;
                }
                "blue" => {
                    bag.blue -= num as i64;
                }
                "green" => {
                    bag.green -= num as i64;
                }
                _ => {
                    panic!("Unknown color {}", color);
                }
            }

            // Check if any color is negative
            if bag.red < 0 || bag.blue < 0 || bag.green < 0 {
                return false;
            }
        }
    }

    return true;
}

fn parse_part2(line: &str) -> i64 {
    let games = line.split(":").collect::<Vec<_>>();
    let game = games[1].trim();
    let matches: Vec<_> = game.split(";").collect();
    let mut max_bag = Match {
        red: 0,
        blue: 0,
        green: 0,
    };

    for m in matches {
        let trimmed_m = m.trim();
        let reveals: Vec<_> = trimmed_m.split(",").collect();

        for r in reveals {
            let mut parts = r.trim().split(" ");
            let (num, color) = (
                parts.next().unwrap().parse::<usize>().unwrap(),
                parts.next().unwrap(),
            );

            match color {
                "red" => {
                    max_bag.red = std::cmp::max(max_bag.red, num as i64);
                }
                "blue" => {
                    max_bag.blue = std::cmp::max(max_bag.blue, num as i64);
                }
                "green" => {
                    max_bag.green = std::cmp::max(max_bag.green, num as i64);
                }
                _ => {
                    panic!("Unknown color {}", color);
                }
            }
        }
    }

    return max_bag.red * max_bag.blue * max_bag.green;
}
