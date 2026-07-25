class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequencies = [0] * 26
        for task in tasks:
            frequencies[ord(task) - ord('A')] += 1
            
        max_freq = 0
        for freq in frequencies:
            if freq > max_freq:
                max_freq = freq
                
        max_freq_tasks_count = 0
        for freq in frequencies:
            if freq == max_freq:
                max_freq_tasks_count += 1
                
        intervals_needed = (max_freq - 1) * (n + 1) + max_freq_tasks_count
        
        return max(len(tasks), intervals_needed)
