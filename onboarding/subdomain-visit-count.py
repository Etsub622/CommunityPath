class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store={}
        for i in cpdomains:
            count,domain=i.split()
            count=int(count)
            subDomains=domain.split('.')
            
            for d in range(len(subDomains)):
                subDomain=".".join(subDomains[d:])
                store[subDomain]=store.get(subDomain,0)+count

            output=[]
            for subDomain,count in store.items():
                output.append(f"{count} {subDomain}")   
        return output     



