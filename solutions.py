from typing import List, Dict
import collections
import math
import re


def load_txt_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as handle:
        content = handle.read().splitlines()
    return content


def problem_1a(data: List[str], target = 2020) -> int:
    data = [int(e) for e in data]
    complementaries = {target-e: e for e in data}

    for e in data:
        if complementaries.get(e):
            return e*complementaries.get(e)

def problem_1b(data: List[str], target: int = 2020) -> int:
    data = sorted([int(e) for e in data])

    for idx, e in enumerate(data):
        low, high = idx+1, len(data)-1
        while low<high:
            if data[low]+data[idx]+data[high]>target:
                high -= 1
            elif data[low]+data[idx]+data[high]<target:
                low+=1
            else:
                return data[low] * data[idx] * data[high]

def problem_2a(data: List[str]) -> int:
    data_parsed = [[w.strip() for w in e.split(":")] for e in data]
    matches = []
    for e in data_parsed:
        boundaries, letter = e[0].split(" ")
        low, high = boundaries.split("-")
        letters = collections.Counter(e[1])
        if int(low)<=letters[letter]<=int(high):
            matches.append(e)
    return len(matches)


def problem_2b(data: List[str]) -> int:
    data_parsed = [[w.strip() for w in e.split(":")] for e in data]
    matches = []
    for e in data_parsed:
        boundaries, letter = e[0].split(" ")
        low, high = boundaries.split("-")
        low_l, high_l = e[1][int(low)-1], e[1][int(high)-1]
        if (int(low_l==letter) + int(high_l==letter)) == 1:
            matches.append(e)
    return len(matches)


def problem_3a(data: List[str], horizontal_skips: List[int], vertical_skip: int = 1) -> List[int]:
    vals = []

    for skip in horizontal_skips:
        trees = 0
        pointer = 0
        horizontal_length = len(data[0])
        for row in data[::vertical_skip]:
            if row[pointer]=="#":
                trees += 1

            pointer+=skip
            if pointer>=horizontal_length:
                pointer = pointer%horizontal_length

        vals.append(trees)
    return vals


def problem_3b(data: List[str]) -> List[int]:
    vals_1 = problem_3a(data, horizontal_skips=[1, 3, 5, 7], vertical_skip=1)
    vals_2 = problem_3a(data, horizontal_skips=[1], vertical_skip=2)
    return math.prod(vals_1) * math.prod(vals_2)


def problem_4_convert_input_to_list_of_dict(data: List[str]) -> List[Dict]:
    regex_key_val = re.compile(r"(\w+):(#{0,1}\w+)")
    vals = [re.findall(regex_key_val, e) for e in "\n".join(data).split("\n\n")]
    return [{k:v for k,v in e} for e in vals]

def problem_4a(data: List[str]) -> int:
    expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passports = problem_4_convert_input_to_list_of_dict(data)
    valid_count = 0
    for passport in passports:
        valid_count += all(field in passport for field in expected_fields)
    return valid_count
