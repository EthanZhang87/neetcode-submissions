class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]

            for email1 in account[1:]:
                graph[email1].add(account[1])
                graph[account[1]].add(email1)
                
                email_to_name[email1] = name

        res = []
        visited = set()

        for email in graph:
            if email not in visited:
                local_res = []
                q = deque([email])
                visited.add(email)

                while q:
                    element = q.popleft()
                    local_res.append(element)

                    for node in graph[element]:
                        if node not in visited:
                            q.append(node)
                            visited.add(node)

                res.append([email_to_name[email]] + sorted(local_res))

        return res