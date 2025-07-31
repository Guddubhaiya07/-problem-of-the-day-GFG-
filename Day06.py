#Powerful Integer
class Solution:
    def powerfulInteger(self, intervals, k):
        events = []

        # Create start and end+1 events
        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))

        # Sort events by position
        events.sort()

        count = 0
        result = -1

        for i in range(len(events)):
            pos, delta = events[i]
            count += delta

            # Check next position
            next_pos = events[i + 1][0] if i + 1 < len(events) else pos

            # If current count >= k, then all values from pos to next_pos - 1 are powerful
            if count >= k:
                result = max(result, next_pos - 1)

        return result
