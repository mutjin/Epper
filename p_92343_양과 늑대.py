def solution(info, edges):
    answer=[]
    
    visited=[0]*len(info)
    
    def dfs(sheep,wolf):
        if sheep>wolf:
            answer.append(sheep)
        else:
            return
        
        for edge in edges:
            parent,child=edge
            if visited[parent] and not visited[child]:
                visited[child]=1
                
                #양
                if info[child]==0:
                    dfs(sheep+1,wolf)
                #늑대
                else:
                    dfs(sheep,wolf+1)
                
                visited[child]=0
    
    visited[0]=1
    dfs(1,0)
    
    return max(answer)