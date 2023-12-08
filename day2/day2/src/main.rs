use std::{
    fs::File,
    io::{self, BufRead},
    path::Path,
    usize,
};

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

    let mut res = 0;

    for (i, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        if parse_game(&line) {
            res += i + 1;
        }
    }

    dbg!(res);
}

fn parse_game(line: &str) -> bool {
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
