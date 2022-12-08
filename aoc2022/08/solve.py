import sys

lines = open(sys.argv[1], 'r').read().strip().split('\n')


def check_visible(seq, idx):
    if len(seq[:idx]) < 1 or len(seq[idx+1:]) < 1:
        return True

    if max(seq[:idx]) < seq[idx] or max(seq[idx+1:]) < seq[idx]:
        return True
    else:
        return False


def check_seq(seq, num):
    score = 0
    for ch in seq:
        if int(num) > int(ch):
            score += 1
        elif int(num) == int(ch):
            score += 1
            break
        else:
            break
    return score


def calc_score(seq, idx):
    num = seq[idx]
    seq_before = seq[:idx][::-1]  # reverse
    seq_after = seq[idx+1:]
    score_before = check_seq(seq_before, num)
    score_after = check_seq(seq_after, num)
    return score_before * score_after


visible = 0
max_score = 0


for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        col = [l[j] for l in lines]  # i-th element in col, j-th element in line
        if check_visible(col, i) or check_visible(line, j):
            visible += 1

        score_col = calc_score(col, i)
        score_row = calc_score(line, j)
        score = score_col * score_row
        if max_score < score:
            max_score = score
        

print(visible)
print(max_score)
