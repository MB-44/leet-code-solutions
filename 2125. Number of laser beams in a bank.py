class Solution:
    def numberOfBeams(bank : list[str]) -> int:
        beams_count = 0
        temp = 0
        for row in bank:
            device_count = row.count("1")
            if device_count == 0:
                continue
            beams_count += temp * device_count
            temp = device_count
        return beams_count

if __name__ == "__main__":
    bank = ["011001","000000","010100","001000"]
    # bank = ["000","111","000"]
    result = Solution.numberOfBeams(bank)
    print(result)