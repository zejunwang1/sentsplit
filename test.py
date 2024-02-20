# coding=utf-8

from sentsplit import split_sentence

def test():
    f = open("check_data.txt", mode="r", encoding="utf-8")
    content = f.read()
    sents, locs = split_sentence(content, min_length=32, max_length=256, return_loc=True)
    assert len(locs) == len(sents)
    for p, sent in zip(locs, sents):
        assert content[p] == sent[0]
        print(sent)

if __name__ == "__main__":
    test()

