class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict = {} 
        for path in paths:
            directory, *files = path.split()  
            for file in files:
                file_name, content = file.split('(')
                file_dict.setdefault(content, []).append(directory + '/' + file_name) 
        return [file_paths for file_paths in file_dict.values() if len(file_paths) > 1]