class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = dict()
        res = []

        for i in cpdomains:
            visit, domain = i.split()
            if domain not in domains:
                domains[domain] = int(visit)
            else:
                domains[domain] += int(visit)

            for i in range(len(domain)):
                if domain[i] == '.':
                    subdomain = domain[i+1:]
                    if subdomain not in domains:
                        domains[subdomain] = int(visit)
                    else:
                        domains[subdomain] += int(visit)

        for i in domains:
            inner = ''
            freq = str(domains[i])
            inner += freq
            inner += ' '
            inner += i
            res.append(inner)

        return res





        