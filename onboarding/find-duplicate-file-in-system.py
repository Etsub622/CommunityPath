class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        store={}
        for i in paths:
            parts=i.split()
            root=parts[0]

            for f in parts[1:]:
                f_name,_,content=f.partition("(")
                if content not in store:
                    store[content]=[]
                store[content].append(root+"/"+f_name)
        output=[]
        for j in store.values():
            if len(j)>1:
                output.append(j)
        return output                   
        