from NodeTree import Block


class FileReader:
    def __init__(self, path:str):
        self.path=path

    def get_block_list(self):
        with open(self.path) as f:
            tmp = f.read()
        tmp = tmp.split("\n")
        recs = tmp[1:]
        block_list=[]
        for rec in recs:
            rec=rec.split(" ")
            b=Block(int(rec[0]), int(rec[1]), int(rec[2]))
            block_list.append(b)
        return block_list

    def get_block_cordi_list(self):
        with open(self.path) as f:
            tmp = f.read()
        tmp = tmp.split("\n")
        recs = tmp[1:]
        block_list=[]
        for rec in recs:
            rec = rec.split(" ")
            print(rec)
            rec = list(map(int, rec))
            block_list.append(rec)
        return block_list

    def get_node(self):
        with open(self.path) as f:
            tmp = f.read()
        tmp = tmp.split("\n")
        node=tmp[0].split(" ")
        return(0, 0, int(node[0]), int(node[1]))